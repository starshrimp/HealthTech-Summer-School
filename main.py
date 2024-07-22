import streamlit as st
import requests

st.title("Patient Questionnaire for Predicting Adhesion Risk")

# Age
age = st.number_input("What is your age?", value=27, min_value=0, max_value=120, step=1)

# Gender
gender = st.selectbox("What is your gender?", ["Male", "Female", "Other"], index=1)

# Height
height = st.number_input("What is your height in centimeters?", value=1.68, min_value=0.0, step=0.1)

# Weight
weight = st.number_input("What is your weight in kilograms?", value=58.0, min_value=0.0, step=0.1)

# Previous Abdominal Surgery
previous_surgery = st.radio("Have you previously undergone abdominal surgery?", ["Yes", "No"], index=0)
if previous_surgery == "Yes":
    number_of_surgeries = st.number_input("If yes, how many abdominal surgeries have you had?", value=1, min_value=0, step=1)

# Smoking
smokes = st.radio("Do you smoke?", ["Yes", "No"], index=1)
if smokes == "Yes":
    cigarettes_per_day = st.number_input("If yes, how many cigarettes do you smoke per day?", min_value=0, step=1)

# Alcohol Consumption
alcohol = st.radio("Do you consume alcohol?", ["Yes", "No"], index=0)
if alcohol == "Yes":
    units_per_week = st.number_input("If yes, how many units of alcohol do you consume per week?", value=2, min_value=0, step=1)

# Chronic Diseases
chronic_diseases = st.radio("Do you have any chronic diseases? (e.g., diabetes, hypertension)", ["Yes", "No"], index=1)
if chronic_diseases == "Yes":
    diseases_list = st.text_input("If yes, please specify:")

# Family History of Adhesions
family_history = st.radio("Do you have a family history of adhesions or related complications?", ["Yes", "No"], index=1)

# Abdominal Infections
abdominal_infection = st.radio("Have you ever had an infection in the abdominal area?", ["Yes", "No"], index=0)

# Medication
medication = st.radio("Do you regularly take any medication?", ["Yes", "No"], index=1)
if medication == "Yes":
    medication_list = st.text_input("If yes, please list:")

# Physical Activity Level
physical_activity = st.selectbox("Rate your level of physical activity:", ["Sedentary", "Lightly active", "Moderately active", "Very active"], index=2)

# Submit Button
if st.button("Submit"):
    # Collecting form data
    form_data = {
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "previous_surgery": previous_surgery,
        "number_of_surgeries": number_of_surgeries if previous_surgery == "Yes" else None,
        "smokes": smokes,
        "cigarettes_per_day": cigarettes_per_day if smokes == "Yes" else None,
        "alcohol": alcohol,
        "units_per_week": units_per_week if alcohol == "Yes" else None,
        "chronic_diseases": chronic_diseases,
        "diseases_list": diseases_list if chronic_diseases == "Yes" else None,
        "family_history": family_history,
        "abdominal_infection": abdominal_infection,
        "medication": medication,
        "medication_list": medication_list if medication == "Yes" else None,
        "physical_activity": physical_activity
    }
    
    # Sending POST request
    response = requests.post("https://hook.eu2.make.com/lxxwvlmie4yq4834xpq4pur3yjupct9b", json=form_data)
    
    if response.status_code == 200:
        st.success("Form submitted successfully!")
    else:
        st.error(f"Failed to submit form. Status code: {response.status_code}")

    # Display Summary
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
