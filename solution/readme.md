# Dataset Analysis and Regression Model

    The goal of this project is to model and evaluate vehicle fuel consumption data. Two sources make up the dataset: `measurements2.xlsx` and `measurements.csv`. I conducted exploratory data analysis, developed hypotheses, and constructed a regression model to estimate fuel usage based on several variables after preprocessing and cleaning the data.

# Dataset Description

    Measurements of vehicle usage, including distance driven, speed, temperature inside and outside the car, weather (sun, rain), and if air conditioning (AC) is present, are included in the dataset.
    There are further categorized aspects like gas type and specialties (special driving circumstances).

# Data Preprocessing

    To produce a single dataset called measures, I concatenated the two dataset files, `measurements.csv` and `measurements2.xlsx`.
    To guarantee data integrity, we examined the dataset for null values, duplicates, and unique values after concatenation.
    In numerical columns, we transformed values separated by commas into dots and used suitable techniques (such mean imputation) to fill in any null values.
    Dummy variables were created by one-hot encoding of the categorical columns.
    Two new columns were added: temp_difference (the difference in temperature between the interior and outdoors) and fuel_efficiency (the distance divided by the consumption).
    To make sure the model is robust, outliers were eliminated from the dataset.
    In order to bring the number columns to a uniform scale, they were finally standardized.

# Exploratory Data Analysis (EDA)

    To have a better understanding of the distribution of the data and possible connections, I used a scatter plot matrix (sns.pairplot) to illustrate the associations between various parameters.
    Two theories were developed and put to the test:
    - Hypothesis 1: Speed and fuel usage are significantly correlated.
    - Hypothesis 2: Fuel usage is greatly impacted by the presence of air conditioning (AC).

# Regression Modeling

    In order to forecast fuel usage based on particular features, I developed a linear regression model.
    The sklearn library was used to train and assess the model.
    Model performance was evaluated using evaluation measures such root mean square error (RMSE), mean squared error (MSE), and R-squared score.
    In addition, a residual plot was created to show the error distribution.

# Conclusion

    Important insights into the variables impacting vehicle fuel usage were obtained from the analysis.
    Based on the chosen features, the regression model performed rather well in forecasting fuel use.
    To increase prediction accuracy and investigate other factors influencing fuel efficiency, more research and model development might be necessary.