# Tech challenge Solution

## Python Libraries used:
- Pandas
- Numpy
- Matplotlib
- Seaborn
- scikit-learn


## Workflow

### Data Exploring and Cleaning
The dataframe I've been working with contains gas oil consumes (L/100km) of E10 oil and SP95 oil with different conditions: distance (km), average speed (km/h), temperature inside the car (°C), the temperature outside the car (°C) anything special that happened, if it was raining, if the air condition was on, if it was sunny enough that the car felt warm when started…. 
<br>There are also two columns saying how much and which gas type was buoght. <br> 
<br>
In order to clean the dataframe I decided to:
- Change the type of the variables in the columns *distance* and *consume* from *string* to *float*
- Deleted rows with contraddictive information (for example about the AC)
- Deleted the column *special* because it didn't add information to the dataser that weren't already expressed in other columns.
- Deleted the columns *temp_inside*, *refill liters*, *refill gas* because they presented a lot of null values; also, weren't really impactful for the total consume
- Added a column with ratio between consume and distance
- Added a column to express the gas type as binary values (E10:0, SP98:1)

<br>
I also looked at the distributions of the *distance* and *speed* values and create functions to remove outliers for both.

### Visualization

Using Tableau I confronted Consume per Distance with Speed and Consume with Distance, using AC, rain and sun as filters. I didn't find a stable difference between the use of E10 and SP98

Here's the link to the results : [Tableau](https://public.tableau.com/app/profile/lucia.aguzzoni/viz/Tech_Challenge_17031784370450/Story2?publish=yes)


### Prediction of E10 and SP98 consumes through Linear Regression

To confront the consume for E10 and SP98 I created a linear regression model using the values in the dataframe. <br>

Then I created a dataframe of 500 rows with random values of distance, speed, temperature outside the car, AC, rain/sun and I predicted the consume for all these cases for both E10 and SP98 using the linear regression model. I repeated this process 15 times and calculated each time the difference between average E10 consumes and average SP98 consume; these were the result:

case 1 <br>
Predicted consume value with E10 is 5.183 liters <br>
Predicted consume value with SP98 is 5.156 liters <br>
case 2 <br>
Predicted consume value with E10 is 5.225 liters <br>
Predicted consume value with SP98 is 5.198 liters <br>
case 3 <br>
Predicted consume value with E10 is 5.228 liters <br>
Predicted consume value with SP98 is 5.201 liters <br>
case 4 <br>
Predicted consume value with E10 is 5.24 liters <br>
Predicted consume value with SP98 is 5.213 liters <br>
case 5 <br>
Predicted consume value with E10 is 5.233 liters <br>
Predicted consume value with SP98 is 5.206 liters <br>
case 6 <br>
Predicted consume value with E10 is 5.228 liters <br>
Predicted consume value with SP98 is 5.201 liters <br>
case 7 <br>
Predicted consume value with E10 is 5.232 liters <br>
Predicted consume value with SP98 is 5.205 liters <br>
case 8 <br>
Predicted consume value with E10 is 5.197 liters <br>
Predicted consume value with SP98 is 5.171 liters <br>
case 9 <br>
Predicted consume value with E10 is 5.208 liters <br>
Predicted consume value with SP98 is 5.181 liters <br>
case 10 <br>
Predicted consume value with E10 is 5.243 liters <br>
Predicted consume value with SP98 is 5.216 liters <br>
case 11 <br>
Predicted consume value with E10 is 5.28 liters <br>
Predicted consume value with SP98 is 5.253 liters <br>
case 12 <br>
Predicted consume value with E10 is 5.24 liters <br>
Predicted consume value with SP98 is 5.214 liters <br>
case 13 <br>
Predicted consume value with E10 is 5.205 liters <br>
Predicted consume value with SP98 is 5.178 liters <br>
case 14 <br>
Predicted consume value with E10 is 5.183 liters <br>
Predicted consume value with SP98 is 5.157 liters <br>
case 15 <br>
Predicted consume value with E10 is 5.218 liters <br>
Predicted consume value with SP98 is 5.192 liters <br> <br>
On Average, the difference between predicted consume value with E10 and predicted consume value with SP98 was 0.03 liters.

## Conclusions
It seems that the E10 oil consume a little bit more than SP98. Anyway, since E10 is generally cheaper than SP98 it may be more convenient to use it. <br>
I think it would be better to spend more time improving the consume prediction and then extract precise information about the cost of E10 and SP98 to get a more accurate answer.




