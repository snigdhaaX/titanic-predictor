import streamlit as st
import joblib
import pandas as pd
import numpy as np

model = joblib.load('titanic_model.pkl')

st.set_page_config(page_title="Titanic Survival Predictor")

st.title(" Titanic Survival Predictor")
st.write("Enter passenger details below to see if they would have survived.")

col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox("Ticket Class", [1, 2, 3], help="1 = Upper, 2 = Middle, 3 = Lower")
    age = st.slider("Age", 0, 100, 25)
    fare = st.number_input("Fare (Ticket Price)", value=32.0)

with col2:
    sex = st.selectbox("Sex", ["Male", "Female"])
    sibsp = st.number_input("Siblings/Spouses Aboard", 0, 10, 0)
    parch = st.number_input("Parents/Children Aboard", 0, 10, 0)
    embarked = st.selectbox("Port of Embarkation", ["S", "C", "Q"])

sex_num = 0 if sex == "Male" else 1
embarked_map = {"S": 0, "C": 1, "Q": 2}
embarked_num = embarked_map[embarked]

#  Prediction Button
if st.button("Calculate Survival Probability"):
    
    features = np.array([[pclass, sex_num, age, sibsp, parch, fare, embarked_num]])
    
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.success("passenger likely to have survived")
        st.balloons()
    else:
        st.error("passenger might have not survived")