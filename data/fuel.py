
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score , mean_squared_error,confusion_matrix , classification_report
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import TomekLinks
import streamlit as st
import pickle
from PIL import Image

import warnings
warnings.filterwarnings('ignore')



st.write("""
# **Technical challenge for COBIFY**:
## Car fuel prediction
#### *The aim of this project will be to the fuel used by every car depending on different variables.*
""")


image=Image.open('D:\WB\Ironhack\careerhack\technical_challenge\data-analytics-challenge\data\png_fuel_79214.png')

st.image(image)




pd.set_option('display.max_columns', None)


df=pd.read_csv('measurements.csv')


num_cols=['distance','consume','speed','temp_inside','temp_outside']
cat_cols=['gas_type','ac','rain','sun']

st.sidebar.write("""
### Please, introduce the following features:
""")
# Categorical variables

ac_var=st.sidebar.selectbox('Air condition?',['no','yes'])
rain_var=st.sidebar.selectbox('Was it rainy?',['yes','no'])
sun_var=st.sidebar.selectbox('Was it sunny?',['yes','no'])

cat_var_list=[sex_var,edu_var,marr_var]

# Numeric variables

distance_var = st.sidebar.number_input('Introduce the distance',min_value=0, max_value=1000)
consume_var = st.sidebar.number_input('Introduce the consume',min_value=0, max_value=10) 
speed_var = st.sidebar.number_input('Introduce the speed',min_value=0, max_value=120) 
temp_in_var =st.sidebar.number_input('Introduce the in the car',min_value=-10, max_value=35)
temp_out_var =st.sidebar.number_input('Introduce the outside',min_value=-10, max_value=35)



# Categorical and numerica dataframes

data_cat={'ac':[ac_var],'rain':[rain_var],'sun':[sun_var]}
data_num={'distance':[distance_var],'consume':[consume_var],'speed':[speed_var],'temp_in':[temp_in_var],'temp_out':[temp_out_var]}




loaded_encoder = pickle.load(open('encoder_model.sav', 'rb'))
loaded_scaled = pickle.load(open('scaled_model.sav', 'rb'))




# Dataframes with the values given by the user

df_cat_user=pd.DataFrame(data_cat)
df_num_user=pd.DataFrame(data_num)

# Scaling numeric df given by the user

# scaler_user=StandardScaler()
df_num_user_sc=loaded_scaled.transform(df_num_user)

# Encoding categorical df given by the user

df_cat_user_enc = loaded_encoder.transform(df_cat_user).toarray()

# Creating the X_test to predict the result with the data provided by the user
#df_num_user_sc
#df_cat_user_enc
X_test_pred=np.concatenate([df_num_user_sc,df_cat_user_enc],axis=1)


loaded_model = pickle.load(open('finalized_model.sav', 'rb'))


y_tl_pred_dt = loaded_model.predict(X_test_pred) 

path=loaded_model.decision_path(X_test_pred)
#path

probab=loaded_model.predict_proba(X_test_pred)
probab
# Hacer el "st.write" con el valor "y_tl_pred_dt" para mostrar el valor de la predicción realizada.

if y_tl_pred_dt=='1':
        st.write("""
                        #### The gas type is SP98
                        """)

elif y_tl_pred_dt=='no':
         st.write("""
                        #### The gas type is E10
                        """)