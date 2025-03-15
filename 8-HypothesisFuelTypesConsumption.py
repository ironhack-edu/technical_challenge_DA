import pandas as pd
from scipy.stats import ttest_ind, mannwhitneyu
import seaborn as sns
import matplotlib.pyplot as plt

comparison_df = pd.read_csv(r"C:\Users\Carlos\Documents\Data Analyst Career Looking\Test\technical_challenge_DA\predictions_random_forest.csv")

price_sp98 = 2.1267  # €/L
price_e10 = 1.4989   # €/L

df_sp98 = comparison_df.copy()
df_e10 = comparison_df.copy()

df_sp98["total_cost"] = df_sp98["Actual"] * price_sp98
df_e10["total_cost"] = df_e10["Actual"] * price_e10

sp98_consume = df_sp98["Actual"].dropna()
e10_consume = df_e10["Actual"].dropna()

t_stat, p_value_ttest = ttest_ind(sp98_consume, e10_consume, equal_var=False)

u_stat, p_value_mannwhitney = mannwhitneyu(sp98_consume, e10_consume, alternative="greater")

print(f"T-test p-value: {p_value_ttest:.5f}")
print(f"Mann-Whitney U-test p-value: {p_value_mannwhitney:.5f}")

sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 5))
sns.boxplot(x=["SP98"] * len(sp98_consume) + ["E10"] * len(e10_consume),
            y=pd.concat([sp98_consume, e10_consume]), 
            palette=["red", "blue"])

plt.ylabel("Fuel Consumption (Liters)")
plt.title("Fuel Consumption Comparison: SP98 vs E10")
plt.show()
