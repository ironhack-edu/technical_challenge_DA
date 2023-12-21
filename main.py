import src.cleaning as cl
import src.linear_regression as lr

path = "data/measurements.csv"

df = cl.import_df(path)

cleaned_df = cl.clean_df(df)
#cl.save_df(cleaned_df,"cleaned_measurements")
cleaned_df_no_outliers = cl.remove_outliers(cleaned_df)
#cl.save_df(cleaned_df_no_outliers,"cleaned_measurements_no_outliers")


num_df = cl.only_numerical(cleaned_df)
linear_reg = lr.lin_regression(num_df)

differences=[]

for i in range(15):
    sample_size = 500
    moke_df = lr.create_moke_df(num_df,sample_size)
    df_E10 = lr.add_gas_type("E10", sample_size, moke_df)
    df_SP98 = lr.add_gas_type("SP98", sample_size, moke_df)

    consume_E10 = lr.predict(linear_reg, df_E10)
    consume_SP98 = lr.predict(linear_reg, df_SP98)

    average_consume_E10 = consume_E10.mean()
    average_consume_SP98 = consume_SP98.mean()
    diff = average_consume_E10 - average_consume_SP98
    differences.append(diff)

    print(f"case {i+1}")
    print(f"Predicted consume value with E10 is {round(average_consume_E10,3)} liters")
    print(f"Predicted consume value with SP98 is {round(average_consume_SP98,3)} liters")

average_diff = sum(differences)/len(differences)
print(f"On Average, the difference between predicted consume value with E10 and predicted consume value with SP98 was {round(average_diff,2)} liters.")
