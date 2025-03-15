import pandas as pd

csv_path = r"C:\Users\Carlos\Documents\Data Analyst Career Looking\Test\technical_challenge_DA\data\measurements.csv"
df_csv = pd.read_csv(csv_path)

excel_path = r"C:\Users\Carlos\Documents\Data Analyst Career Looking\Test\technical_challenge_DA\data\measurements2.xlsx"
df_excel = pd.read_excel(excel_path)

df_csv = df_csv.replace(',', '.', regex=True)

df_csv = df_csv.astype({
    "distance": float,
    "consume": float,
    "speed": float,
    "temp_inside": float,
    "temp_outside": float,
    "AC": int,
    "rain": int,
    "sun": int,
    "refill liters": float
})

df_csv["temp_inside"] = pd.to_numeric(df_csv["temp_inside"], errors="coerce")
df_excel["temp_inside"] = pd.to_numeric(df_excel["temp_inside"], errors="coerce")

df_csv["distance"] = pd.to_numeric(df_csv["distance"], errors="coerce")

df_csv["temp_inside"].fillna(df_csv["temp_inside"].median(), inplace=True)
df_excel["temp_inside"].fillna(df_excel["temp_inside"].median(), inplace=True)

df_csv.drop(columns=["specials"], inplace=True)
df_excel.drop(columns=["specials"], inplace=True)

df_csv["refilled"] = df_csv["refill liters"].apply(lambda x: 1 if pd.notna(x) else 0)
df_excel["refilled"] = df_excel["refill liters"].apply(lambda x: 1 if pd.notna(x) else 0)

df_csv["refill gas"].fillna("No Refill", inplace=True)
df_excel["refill gas"].fillna("No Refill", inplace=True)

df_csv["consume"] = pd.to_numeric(df_csv["consume"], errors="coerce")
df_excel["consume"] = pd.to_numeric(df_excel["consume"], errors="coerce")

print(df_csv.info())
print(df_excel.info())
print(df_csv.isnull().sum())
print(df_excel.isnull().sum())

df_combined = pd.concat([df_csv, df_excel], ignore_index=True)

duplicates = df_combined.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

df_combined = df_combined.drop_duplicates()

from sklearn.model_selection import train_test_split

features = ["distance", "speed", "temp_inside", "temp_outside", "AC", "rain", "sun"]
target = "consume"

df_ml = df_combined.dropna(subset=features + [target])

X_train, X_test, y_train, y_test = train_test_split(df_ml[features], df_ml[target], test_size=0.2, random_state=42)

print(f"Training data: {X_train.shape}")
print(f"Test data: {X_test.shape}")

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

coef_dict = dict(zip(features, model.coef_))

print("Model Coefficients:")
for feature, coef in coef_dict.items():
    print(f"{feature}: {coef:.4f}")

print(f"Intercept: {model.intercept_:.4f}")

from sklearn.metrics import mean_absolute_error, r2_score

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"R-squared (R²): {r2:.4f}")

#From the API in import requests py

price_sp98 = 2.1267  #€/L
price_e10 = 1.4989   #€/L

df_sp98 = df_combined[df_combined["gas_type"] == "SP98"].copy()
df_e10 = df_combined[df_combined["gas_type"] == "E10"].copy()

df_sp98["total_cost"] = df_sp98["consume"] * price_sp98
df_e10["total_cost"] = df_e10["consume"] * price_e10

print(f"Average cost per trip (SP98): {df_sp98['total_cost'].mean():.2f}€")
print(f"Average cost per trip (E10): {df_e10['total_cost'].mean():.2f}€")

print(df_sp98[["consume", "total_cost"]].head())
print(df_e10[["consume", "total_cost"]].head())

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 5))
sns.boxplot(x=["SP98"] * len(df_sp98["total_cost"]) + ["E10"] * len(df_e10["total_cost"]),
            y=pd.concat([df_sp98["total_cost"], df_e10["total_cost"]]), 
            palette=["red", "blue"])

plt.ylabel("Total Cost (€)")
plt.title("Comparison of Fuel Costs per Trip (SP98 vs E10)")
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(df_sp98["total_cost"], bins=20, color="red", label="SP98", kde=True, alpha=0.6)
sns.histplot(df_e10["total_cost"], bins=20, color="blue", label="E10", kde=True, alpha=0.6)
plt.xlabel("Total Cost (€)")
plt.ylabel("Frequency")
plt.title("Distribution of Fuel Costs per Trip")
plt.legend()
plt.show()

average_costs = [df_sp98["total_cost"].mean(), df_e10["total_cost"].mean()]
labels = ["SP98", "E10"]

plt.figure(figsize=(7, 5))
sns.barplot(x=labels, y=average_costs, palette=["red", "blue"])
plt.ylabel("Average Cost per Trip (€)")
plt.title("Average Fuel Cost per Trip: SP98 vs E10")
plt.show()
