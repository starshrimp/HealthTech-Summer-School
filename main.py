import streamlit as st

st.title("Patient Questionnaire for Predicting Adhesion Risk")

# Age
age = st.number_input("What is your age?", min_value=0, max_value=120, step=1)

# Gender
gender = st.selectbox("What is your gender?", ["Male", "Female", "Other"])

# Height
height = st.number_input("What is your height in centimeters?", min_value=0.0, step=0.1)

# Weight
weight = st.number_input("What is your weight in kilograms?", min_value=0.0, step=0.1)

# Previous Abdominal Surgery
previous_surgery = st.radio("Have you previously undergone abdominal surgery?", ["Yes", "No"])
if previous_surgery == "Yes":
    number_of_surgeries = st.number_input("If yes, how many abdominal surgeries have you had?", min_value=0, step=1)

# Smoking
smokes = st.radio("Do you smoke?", ["Yes", "No"])
if smokes == "Yes":
    cigarettes_per_day = st.number_input("If yes, how many cigarettes do you smoke per day?", min_value=0, step=1)

# Alcohol Consumption
alcohol = st.radio("Do you consume alcohol?", ["Yes", "No"])
if alcohol == "Yes":
    units_per_week = st.number_input("If yes, how many units of alcohol do you consume per week?", min_value=0, step=1)

# Chronic Diseases
chronic_diseases = st.radio("Do you have any chronic diseases? (e.g., diabetes, hypertension)", ["Yes", "No"])
if chronic_diseases == "Yes":
    diseases_list = st.text_input("If yes, please specify:")

# Family History of Adhesions
family_history = st.radio("Do you have a family history of adhesions or related complications?", ["Yes", "No"])

# Abdominal Infections
abdominal_infection = st.radio("Have you ever had an infection in the abdominal area?", ["Yes", "No"])

# Medication
medication = st.radio("Do you regularly take any medication?", ["Yes", "No"])
if medication == "Yes":
    medication_list = st.text_input("If yes, please list:")

# Physical Activity Level
physical_activity = st.selectbox("Rate your level of physical activity:", ["Sedentary", "Lightly active", "Moderately active", "Very active"])

# Submit Button
if st.button("Submit"):
    st.write("### Summary of Your Responses")
    st.write(f"Age: {age}")
    st.write(f"Gender: {gender}")
    st.write(f"Height: {height} cm")
    st.write(f"Weight: {weight} kg")
    
    if previous_surgery == "Yes":
        st.write(f"Previous Abdominal Surgeries: {number_of_surgeries}")
    else:
        st.write("Previous Abdominal Surgeries: No")
    
    if smokes == "Yes":
        st.write(f"Cigarettes per Day: {cigarettes_per_day}")
    else:
        st.write("Smokes: No")
    
    if alcohol == "Yes":
        st.write(f"Units of Alcohol per Week: {units_per_week}")
    else:
        st.write("Consumes Alcohol: No")
    
    if chronic_diseases == "Yes":
        st.write(f"Chronic Diseases: {diseases_list}")
    else:
        st.write("Chronic Diseases: No")
    
    st.write(f"Family History of Adhesions: {family_history}")
    st.write(f"Abdominal Infection: {abdominal_infection}")
    
    if medication == "Yes":
        st.write(f"Medication: {medication_list}")
    else:
        st.write("Medication: No")
    
    st.write(f"Physical Activity Level: {physical_activity}")
