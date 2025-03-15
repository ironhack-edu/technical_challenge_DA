# %%% Celda1
import pandas as pd

csv_path = r"C:\Users\Carlos\Documents\Data Analyst Career Looking\Test\technical_challenge_DA\data\measurements.csv"
df_csv = pd.read_csv(csv_path)

excel_path = r"C:\Users\Carlos\Documents\Data Analyst Career Looking\Test\technical_challenge_DA\data\measurements2.xlsx"
df_excel = pd.read_excel(excel_path)

print(df_csv.head())
print(df_excel.head())

print(df_csv.info())
print(df_excel.info())

print(df_csv.describe())
print(df_excel.describe())
# %%Celda2
import pandas as pd

csv_path = r"C:\Users\Carlos\Documents\Data Analyst Career Looking\Test\technical_challenge_DA\data\measurements.csv"
df_csv = pd.read_csv(csv_path)

excel_path = r"C:\Users\Carlos\Documents\Data Analyst Career Looking\Test\technical_challenge_DA\data\measurements2.xlsx"
df_excel = pd.read_excel(excel_path)

df_csv = df_csv.replace(',', '.', regex=True)

df_scv = df_csv.astype({
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

print(df_csv.isnull().sum())
print(df_excel.isnull().sum())

print(df_csv["temp_inside"].dtype)
print(df_csv["temp_inside"].unique())

df_csv["temp_inside"] = pd.to_numeric(df_csv["temp_inside"], errors="coerce")
df_excel["temp_inside"] = pd.to_numeric(df_excel["temp_inside"], errors="coerce")

df_csv["temp_inside"].fillna(df_csv["temp_inside"].median(), inplace=True)
df_excel["temp_inside"].fillna(df_excel["temp_inside"].median(), inplace=True)

print(df_csv.isnull().sum())
print(df_excel.isnull().sum())

df_csv["refilled"] = df_csv["refill liters"].apply(lambda x: 1 if pd.notna(x) else 0)
df_excel["refilled"] = df_excel["refill liters"].apply(lambda x: 1 if pd.notna(x) else 0)

df_csv["refill gas"].fillna("No Refill", inplace=True)
df_excel["refill gas"].fillna("No Refill", inplace=True)

print(df_csv[["refill liters", "refill gas", "refilled"]].head(15))
print(df_excel[["refill liters", "refill gas", "refilled"]].head(15))

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(df_csv["consume"], bins=30, edgecolor="black", alpha=0.7)
plt.xlabel("Consumo (litros)")
plt.ylabel("Frecuencia")
plt.title("Distribución del consumo de combustible")
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
sns.boxplot(y=df_csv["consume"])
plt.ylabel("Consumo (litros)")
plt.title("Boxplot del consumo de combustible")

plt.tight_layout()
plt.show()

df_csv["consume"] = pd.to_numeric(df_csv["consume"], errors="coerce")


Q1 = df_csv["consume"].quantile(0.25)
Q3 = df_csv["consume"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df_csv[(df_csv["consume"] < lower_bound) | (df_csv["consume"] > upper_bound)]

print(outliers)

plt.figure(figsize=(10, 6))
corr = df_csv.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt= ".2f", linewidths=0.5)
plt.title("Matriz de correlación entre variables")
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df_csv["speed"], df_csv["consume"], alpha=0.5)
plt.xlabel("Velocidad (km/h)")
plt.ylabel("Consumo (litros)")
plt.title("Relación entre velocidad y consumo de combustible")
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df_csv["distance"], df_csv["consume"], alpha=0.5)
plt.xlabel("Distancia (km)")
plt.ylabel("Consumo (litros)")
plt.title("Relación entre distancia y cnsumo de combustible")
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x=df_csv["gas_type"], y=df_csv["consume"])
plt.xlabel("Tipo de Gasolina")
plt.ylabel("consumo (litros)")
plt.title("Consumo de combustible por tipo de gasolina")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()