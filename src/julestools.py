import pandas as pd
import numpy as np
from sklearn.utils import resample
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder, OrdinalEncoder
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, ConfusionMatrixDisplay
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble  import RandomForestClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import NuSVC
import xgboost as xgb
from sklearn import svm

def fix_col_names(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(r'\s+','_',regex=True)
    return df

def nan_to_null(df, cols=None):
    if cols is None: cols = df.columns.tolist()
    [df[k].fillna(0, inplace=True) for k in cols ]

def get_df_name(df):
    return [x for x in globals() if globals()[x] is df][0]

def df_shape(list_of_dfs):
    for df in list_of_dfs:  
        print(f"{get_df_name(df)}: {df.shape[0]} rows, {df.shape[1]} columns")


def scaling(df, features, target, method=MinMaxScaler()):
    X , y = df[features] , df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=1)
    scaler = method.fit(X_train)
    X_train_scaled = pd.DataFrame(scaler.transform(X_train),columns=X.columns)
    X_test_scaled  = pd.DataFrame(scaler.transform(X_test), columns=X.columns)
    y_train = y_train.reset_index(drop=True)
    y_test = y_test.reset_index(drop=True)
    return X_train_scaled, X_test_scaled, y_train, y_test

def model_fit_predict(model, X_train_scaled, X_test_scaled, y_train, y_test):
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    return y_pred

def eval_model(note, model, X_test, y_test, results, label_type=1):
    y_pred = model.predict(X_test)
    score = model.score(X_test, y_test)
    precision = precision_score(y_test,y_pred, pos_label=label_type)
    recall = recall_score(y_test, y_pred, pos_label='Yes')
    f1 = f1_score(y_test, y_pred, pos_label='Yes')
    false_negatives = confusion_matrix(y_test, y_pred)[1][0]
    new_result = pd.DataFrame({'note':note,'accuracy':score,'precision':precision,'recall':recall,'f1_score':f1,'false_negatives':false_negatives},index=[0])
    return pd.concat([results,new_result],axis=0)

def eval_report(y_test,y_pred):
    return print(classification_report(y_test, y_pred),"accuracy score : {:.2f}".format(accuracy_score(y_test, y_pred)))
