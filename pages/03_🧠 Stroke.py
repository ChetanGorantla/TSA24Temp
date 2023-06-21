import streamlit as st
import joblib
import pandas as pd
import pickle

st.set_page_config(page_title="Diabetes Predictor", page_icon="🧠")
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
st.markdown("# Stroke Predictor")
st.write("Input your symptoms below")

age = st.number_input("How old are you?", value=25, min_value=25, max_value=100) 
option = st.selectbox(
    'What is your sex?',
    ('Male', 'Female'))

col1, col2 = st.columns(2)

avg_glucose_level = col1.number_input("What is your average glucose level?", value = 0, min_value = 0, max_value = 300)
bmi = col1.number_input("What is your BMI (Body Mass Index)?", value = 20, min_value = 20, max_value = 40)
hypertension = col1.checkbox("Do you have hypertension?")
heart_disease = col1.checkbox("Do you have heart disease?")

married = col2.checkbox("Are you married?")
work_type = col2.selectbox("What is your form of work?", ("Private", "Self-employed", "Govt. job"))
residence_type = col2.selectbox("What is your area of residency?", ("Urban","Rural"))
smoking_status = col2.selectbox("What is your smoking status?", ("Never smokes", "Formerly smoked", "Smokes", "Unknown"))
                                                          


