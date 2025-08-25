import streamlit as st
import pickle
import numpy as np


with open("exam_model.sav", "rb") as f:
    model = pickle.load(f)

st.title("📘 Student Exam Pass/Fail Predictor")

st.write("Enter student details to predict whether they will Pass or Fail:")

hours_studied = st.number_input("Hours Studied", min_value=0, max_value=12, value=5)
sleep_hours = st.number_input("Sleep Hours", min_value=0, max_value=12, value=7)
class_attendance = st.number_input("Class Attendance (%)", min_value=50, max_value=100, value=75)

if st.button("Predict Result"):
    features = np.array([[hours_studied, sleep_hours, class_attendance]])
    prediction = model.predict(features)[0]
    
    if prediction == 1:
        st.success("✅ Student is likely to PASS!")
    else:
        st.error("❌ Student is likely to FAIL.")
