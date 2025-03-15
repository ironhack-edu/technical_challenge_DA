import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import GridSearchCV
import numpy as np
import joblib

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

df_combined = pd.concat([df_csv, df_excel], ignore_index=True)

duplicates = df_combined.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

df_combined = df_combined.drop_duplicates()

from sklearn.model_selection import train_test_split

features = ["distance", "speed", "temp_inside", "temp_outside", "AC", "rain", "sun"]
target = "consume"

df_ml = df_combined.dropna(subset=features + [target])

X_train, X_test, y_train, y_test = train_test_split(df_ml[features], df_ml[target], test_size=0.2, random_state=42)

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)

mae_rf = mean_absolute_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

rf_model = RandomForestRegressor(random_state=42)

param_grid = {
     "n_estimators": [100, 300, 500],
     "max_depth": [10, 20, None],
     "min_samples_split": [2, 4, 6],
     "min_samples_leaf": [1, 2, 3]
}

grid_search = GridSearchCV(
     estimator=rf_model,
     param_grid=param_grid,
     scoring="neg_mean_absolute_error",
     cv=5,
     n_jobs=-1
)

grid_search.fit(X_train, y_train)

best_params = grid_search.best_params_
best_model = grid_search.best_estimator_

y_pred = best_model.predict(X_test)

mae_best = mean_absolute_error(y_test, y_pred)
r2_best = r2_score(y_test, y_pred)

comparison_df = pd.DataFrame({"Actual": y_test.values, "Predicted": y_pred})

print("Comparison of actual vs predicted values:")
print(comparison_df.head(10))

comparison_df["Absolute Error"] = np.abs(comparison_df["Actual"] - comparison_df["Predicted"])

print(f"Mean Absolute Error: {comparison_df['Absolute Error'].mean():.4f}")

comparison_df.to_csv(r"C:\Users\Carlos\Documents\Data Analyst Career Looking\Test\technical_challenge_DA\predictions_random_forest.csv", index=False)
print("Predictions saved in predictions_random_forest.csv")

joblib.dump(best_model, r"C:\Users\Carlos\Documents\Data Analyst Career Looking\Test\technical_challenge_DA\best_random_forest_model.pkl")

print("Model saved as best_random_forest_model.pkl")
