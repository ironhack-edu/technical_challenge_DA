import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

best_model = joblib.load("best_random_forest_model.pkl")

features = ["distance", "speed", "temp_inside", "temp_outside", "AC", "rain", "sun"]

feature_importances = best_model.feature_importances_

importance_df = pd.DataFrame({"Feature": features, "Importance": feature_importances})

importance_df = importance_df.sort_values(by="Importance", ascending=False)

print("Feature Importance in Random Forest Model:")
print(importance_df)

plt.figure(figsize=(8, 5))
sns.barplot(x=importance_df["Importance"], y=importance_df["Feature"], palette="viridis")
plt.xlabel("Importance Score")
plt.ylabel("Feature")
plt.title("Feature Importance in Fuel Consumption Prediction")
plt.show()
