import streamlit as st
import pandas as pd
import numpy as np
from autogluon.tabular import TabularPredictor


st.title('Telco Customer Churn prediction')
gender = st.selectbox("gender", options = ["Male","Female"])
SeniorCitizen = st.selectbox("SeniorCitizen", options = ["0","1"])
Dependents = st.selectbox ("Partner", option=['Yes','No'])
tenure = st.number_input('tenure')
DPhoneService = st.selectbox('PhoneService', options=['Yes', 'No'])
Multiplelines = st.selectbox('Multiplelines', options = ['No phone service', 'No', 'Yes'])
InternetService = st.selectbox('InternetService', options = ['DSL', 'Fibre optic', 'No'])
OnlineSecurity = st.selectbox('Onlinesecurity', options= ['Yes', 'No'])


PaperlessBilling = st.selectbox('PaperBilling', options = ['Yes', 'No'])
PaymentMethod = st.selectbox('PaymentMethod', options = ['Elctronic check', 'Mailed check', 'Bank transfer (automatic)', 'Crdeit card (automatic)'])
MonthlyCHarges = st.number_input('MonthlyCharges')
TotalCharges = st.number_input('TotalCharges')

MonthlyCharges = st.number_input('MonthlyCharges', 0, 1000)
TotalCharges = st.number_input('TotalCharges', 0, 2000)