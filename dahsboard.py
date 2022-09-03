import pandas as pandas
import numpy as np
import streamlit as st
import seaborn as sns

sns.set_style('darkgrid')

st.title('Dashboard for comparing comsuptions and kilometers')

def load_data():
    df = pd.read_excel("df3.df3.xlsx")

    return df
   
data = load_data()
numeric_columns = data.select_dtypes(['float64','float32','int32', 'int64']).columns
print(numeric_columns)

st.dataframe(data=data)

checkbox = st.sidebar.checkbox("Reveal data.")
print(checkbox)

if checkbox:
    st.dataframe(data=data)


st.sidebar.subheader("Scatter plot setup")
select_box1 = st.sidebar.selectbox(label='X axis', options=numeric_columns)
print(select_box1)
select_box2 = st.sidebar.selectbox(label='Y axis', options=numeric_columns)
print(select_box2)

sns.relplot(x=select_box1, y=select_box2, data=data)
st.pyplot()