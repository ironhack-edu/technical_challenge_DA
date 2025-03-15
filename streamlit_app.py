import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from scipy.stats import ttest_ind, mannwhitneyu

# Webiste
st.set_page_config(page_title="Fuel Consumption Analysis", layout="wide")

# Model and data
comparison_df = pd.read_csv(r"C:\Users\Carlos\Documents\Data Analyst Career Looking\Test\technical_challenge_DA\predictions_random_forest.csv")
best_model = joblib.load(r"C:\Users\Carlos\Documents\Data Analyst Career Looking\Test\technical_challenge_DA\best_random_forest_model.pkl")

# Features
features = ["distance", "speed", "temp_inside", "temp_outside", "AC", "rain", "sun"]

# Title
st.title("Fuel Consumption Prediction Dashboard")

# Feature importances
st.subheader("Feature Importance")
feature_importances = best_model.feature_importances_
importance_df = pd.DataFrame({"Feature": features, "Importance": feature_importances}).sort_values(by="Importance", ascending=False)
st.dataframe(importance_df)

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=importance_df["Importance"], y=importance_df["Feature"], palette="viridis", ax=ax)
ax.set_xlabel("Importance Score")
ax.set_ylabel("Feature")
ax.set_title("Feature Importance in Fuel Consumption Prediction")
st.pyplot(fig)

# Actual vs Predicted data
st.subheader("Actual vs Predicted Fuel Consumption")
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(x=comparison_df["Actual"], y=comparison_df["Predicted"], alpha=0.7, ax=ax)
ax.plot([comparison_df["Actual"].min(), comparison_df["Actual"].max()], [comparison_df["Actual"].min(), comparison_df["Actual"].max()], linestyle="--", color="red", label="Perfect Fit (y=x)")
ax.set_xlabel("Actual Consumption")
ax.set_ylabel("Predicted Consumption")
ax.set_title("Actual vs. Predicted Fuel Consumption")
ax.legend()
st.pyplot(fig)

st.subheader("Distribution of Prediction Errors")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(comparison_df["Absolute Error"], bins=20, kde=True, color="blue", alpha=0.7, ax=ax)
ax.set_xlabel("Absolute Error")
ax.set_ylabel("Frequency")
ax.set_title("Distribution of Prediction Errors")
st.pyplot(fig)

#Fuel Prices (from API api.precioil.es/api-docs/#/)
price_sp98 = 2.1267 #€/L
price_e10 = 1.4989 #€/L

st.subheader("Fuel Cost Comparison: E10 vs SP98")
df_sp98 = comparison_df.copy()
df_e10 = comparison_df.copy()

df_sp98["total_cost"] = df_sp98["Actual"] * price_sp98
df_e10["total_cost"] = df_e10["Actual"] * price_e10

#Average cost per trip
avg_cost_sp98 = df_sp98["total_cost"].mean()
avg_cost_e10 = df_e10["total_cost"].mean()

st.write(f"Average cost per trip (SP98):** {avg_cost_sp98:.2f}€")
st.write(f"Average cost per trip (E10):** {avg_cost_e10:.2f}€")

fig, ax = plt.subplots(figsize=(6, 4))
sns.barplot(x=["SP98", "E10"], y=[avg_cost_sp98, avg_cost_e10], palette=["red", "green"], ax=ax)
ax.set_ylabel("Average Cost (€)")
ax.set_title("Comparison of Average Fuel Costs per Trip")
st.pyplot(fig)

# Fuel Cost Distribution Comparison

st.subheader("Fuel Cost Distribution: E10 vs SP98")

fig, ax = plt.subplots(figsize=(10, 5))

sns.histplot(df_sp98["total_cost"], bins=20, color="red", label="SP98", kde=True, alpha=0.6, ax=ax)
sns.histplot(df_e10["total_cost"], bins=20, color="blue", label="E10", kde=True, alpha=0.6, ax=ax)

ax.set_xlabel("Total Cost (€)")
ax.set_ylabel("Frequency")
ax.set_title("Distribution of Fuel Costs per Trip")
ax.legend()

st.pyplot(fig)

#Hypothesis E10 vs SP98 differences

st.subheader("Hypothesis Testing: Is There a Significant Difference Between E10 and SP98?")

sp98_consume = df_sp98["Actual"].dropna()
e10_consume = df_e10["Actual"].dropna()

t_stat, p_value_ttest = ttest_ind(sp98_consume, e10_consume, equal_var=False)

u_stat, p_value_mannwhitney = mannwhitneyu(sp98_consume, e10_consume, alternative="greater")

st.write(f"T-test p-value: **{p_value_ttest:.5f}**")
st.write(f"Mann-Whitney U-test p-value: **{p_value_mannwhitney:.5f}**")

if p_value_ttest < 0.05:
    st.success("There is a statistically significant difference in fuel consumption between E10 and SP98.")
else:
    st.warning("No significant difference detected in fuel consumption between E10 and SP98.")

st.subheader("Fuel Consumption Comparison: SP98 vs E10")

fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(x=["SP98"] * len(sp98_consume) + ["E10"] * len(e10_consume),
            y=pd.concat([sp98_consume, e10_consume]), 
            palette=["red", "blue"], ax=ax)

ax.set_ylabel("Fuel Consumption (Liters)")
ax.set_title("Comparison of Fuel Consumption: SP98 vs E10")

st.pyplot(fig)

# Input for new predictions
st.subheader("Make a Prediction")
input_data = {}
for feature in features:
    if feature in ["AC", "rain", "sun"]:
        input_data[feature] = st.radio(f"{feature} (0 = No, 1 = Yes)", [0, 1])
    else:
        input_data[feature] = st.number_input(f"Enter {feature}", min_value=0.0, value=10.0)

# Select fuel type
fuel_type = st.radio("Select Fuel Type", ["E10", "SP98"])

# Button
if st.button("Predict Fuel Consumption"):
    user_input_df = pd.DataFrame([input_data])

    predicted_consumption = best_model.predict(user_input_df)[0]

    price_per_liter = price_e10 if fuel_type == "E10" else price_sp98
    total_cost = predicted_consumption * price_per_liter

    st.success(f"Predicted Fuel Consumption: {predicted_consumption:.2f} liters")
    st.success(f"Estimated Cost for {fuel_type}: {total_cost:.2f}€")

