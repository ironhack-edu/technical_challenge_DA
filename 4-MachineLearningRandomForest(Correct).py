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

df_combined = pd.concat([df_csv, df_excel], ignore_index=True)

duplicates = df_combined.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

df_combined = df_combined.drop_duplicates()

from sklearn.model_selection import train_test_split

features = ["distance", "speed", "temp_inside", "temp_outside", "AC", "rain", "sun"]
target = "consume"

df_ml = df_combined.dropna(subset=features + [target])

X_train, X_test, y_train, y_test = train_test_split(df_ml[features], df_ml[target], test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)

mae_rf = mean_absolute_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

print(f"Random Forest - Mean Absolute Error (MAE): {mae_rf:.4f}")
print(f"Random Forest - R-squared (R²): {r2_rf:.4f}")

#I use hyperparamethers and test some different combinations:

param_grid = [
    {"n_estimators": 100, "max_depth": None, "min_samples_split": 2, "min_samples_leaf": 1},
    {"n_estimators": 200, "max_depth": 15, "min_samples_split": 4, "min_samples_leaf": 2},
    {"n_estimators": 300, "max_depth": 10, "min_samples_split": 5, "min_samples_leaf": 3},
    {"n_estimators": 500, "max_depth": 20, "min_samples_split": 3, "min_samples_leaf": 2},
]

best_mae = float("inf")
best_r2 = 0
best_params = {}

for params in param_grid:
    model = RandomForestRegressor(
        n_estimators=params["n_estimators"],
        max_depth=params["max_depth"],
        min_samples_split=params["min_samples_split"],
        min_samples_leaf=params["min_samples_leaf"],
        random_state=42
    )

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Parameters tested: {params}")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"R-squared (R²): {r2:.4f}")
print("-----")

if mae < best_mae:
      best_mae = mae
      best_r2 = r2
      best_params = params
    
print("\nBest Hyperparameters found:")
print(best_params)
print(f"Best MAE: {best_mae:.4f}")
print(f"Best R²: {best_r2:.4f}")

#As far as results are slightly worst than normal RandomForestTest this didn't got any better, so i will decide authomatically the best hyperparameters using GridSearchCV:

from sklearn.model_selection import GridSearchCV

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

print("Best Hyperparameters found:")
print(best_params)
print(f"Best Mean Absolute Error (MAE): {mae_best:.4f}")
print(f"Best R-squared (R²): {r2_best:.4f}")

