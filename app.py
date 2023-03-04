import streamlit as st


st.title("Predict whether a customer will stay or not")
payment_method = st.selectbox(
                              "PaymentMethod", options=['Electronic check', 
                              'Bank transfer (automatic)', 'Mailed check',
                              'Credit card (automatic)']
)

senior_citizen = st.selectbox('SeniorCitizen', options=['0','1'])
multiple_lines = st.selectbox('MultipleLines', options=['No phone service', 'Yes', 'No'])
tenure = st.slider('tenure', 1, 64)