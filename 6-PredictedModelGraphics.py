import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

comparison_df = pd.read_csv("predictions_random_forest.csv")

plt.figure(figsize=(8, 6))
sns.scatterplot(x=comparison_df["Actual"], y=comparison_df["Predicted"], alpha=0.7)
plt.plot(
    [comparison_df["Actual"].min(), comparison_df["Actual"].max()],
    [comparison_df["Actual"].min(), comparison_df["Actual"].max()],
    linestyle="--", color="red", label="Perfect Fit (y=x)"
)
plt.xlabel("Actual Consumption")
plt.ylabel("Predicted Consumption")
plt.title("Actual vs. Predicted Fuel Consumption")
plt.legend()
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(comparison_df["Absolute Error"], bins=20, kde=True, color="blue", alpha=0.7)
plt.xlabel("Absolute Error")
plt.ylabel("Frequency")
plt.title("Distribution of Prediction Errors")
plt.show()