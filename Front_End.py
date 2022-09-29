import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

def main():
	
	km = st.number_input("Kilometers of your trip:", 0)
	temp_out = st.number_input("Outside temperature:", 0)
	temp_in = st.number_input("Car temperature:", 0)
	
	gas = st.selectbox("Type of gas:", ["E10", "SP98"])
	if gas == "E10":
		gas = 1
	else:
		gas = 0
		
	ac = st.selectbox("Do you have the AC on?", ["Yes", "No"])
	if ac == "Yes":
		ac = 1
	else:
		ac = 0
		
	rain = st.selectbox("Is it raining?", ["Yes", "No"])
	if rain == "Yes":
		rain = 1
	else:
		rain = 0
		
	sun = st.selectbox("Is the car already warmed?", ["Yes", "No"])
	if sun == "Yes":
		sun = 1
	else:
		sun = 0
		
	data1 = pd.Series([km, temp_out, temp_in])
	df1 = pd.DataFrame([list(data1)], columns = ["distance", "temp_inside", "temp_outside"])
	
	data2 = pd.Series([gas, ac, rain, sun])
	df2 = pd.DataFrame([list(data2)], columns = ["gas_type", "ac", "rain", "sun"])
	
	with open("transformer.pkl", "rb") as file:
		transformer = pickle.load(file)
	df1 = transformer.transform(df1)
	
	with open("scaler.pkl", "rb") as file:
		scaler = pickle.load(file)
	df1 = scaler.transform(df1)
	
	df1 = pd.DataFrame(df1)
	
	df = pd.concat([df1, df2], axis = 1)
	
	with open("model.pkl", "rb") as file:
		model = pickle.load(file)
	result = model.predict(df)
	
	st.write("Your cost per km is:",round(result[0],2),"€")
	
main()