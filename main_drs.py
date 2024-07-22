import streamlit as st
import requests

st.title("Doctor Questionnaire for Predicting Adhesion Risk")

# Type of Surgery Planned
surgery_type = st.selectbox("Type of Surgery Planned", ["Diagnostic endoscopy", "Therapeutic endoscopy", "Laparoscopic surgery", "Open abdominal surgery", "Other"], index=None)

# Estimated Duration of Surgery (in hours)
duration = st.number_input("Estimated Duration of Surgery (in hours)", min_value=0.0, step=0.1)

# Emergency Surgery
emergency = st.radio("Is the surgery being performed as an emergency?", ["Yes", "No"], index=None)

# Extent of Surgical Intervention
intervention_extent = st.selectbox("Extent of Surgical Intervention", ["Minor", "Moderate", "Extensive"], index=None)

# Planned Use of Anti-Adhesion Barriers
anti_adhesion_barriers = st.radio("Planned Use of Anti-Adhesion Barriers", ["Yes", "No"], index=None)

# Expected Blood Loss (ml)
blood_loss = st.number_input("Expected Blood Loss (ml)", min_value=0, step=1)

# Presence of Pre-existing Adhesions Identified in Imaging
pre_existing_adhesions = st.radio("Presence of Pre-existing Adhesions Identified in Imaging?", ["Yes", "No"], index=None)

# Previous Surgeries in the Same Area
previous_area_surgeries = st.radio("Previous Surgeries in the Same Area?", ["Yes", "No"], index=None)

# Patient's BMI (Body Mass Index)
bmi = st.number_input("Patient's BMI (Body Mass Index)", min_value=0.0, step=0.1)

# Planned Use of Medications Known to Influence Adhesion Formation
medications_influence_adhesions = st.radio("Any planned use of medications known to influence adhesion formation (e.g., steroids, anticoagulants)?", ["Yes", "No"], index=None)
if medications_influence_adhesions == "Yes":
    medication_details = st.text_input("If yes, please specify:")

# Surgeon's Experience Level
surgeon_experience = st.selectbox("Surgeon's experience level with the specific procedure", ["Novice", "Intermediate", "Expert"], index=None)

# Intraoperative Complications Anticipated
anticipated_complications = st.radio("Intraoperative Complications Anticipated?", ["Yes", "No"], index=None)

# Presence of Co-morbid Conditions Affecting Healing
co_morbid_conditions = st.radio("Presence of Co-morbid Conditions Affecting Healing?", ["Yes", "No"], index=None)
if co_morbid_conditions == "Yes":
    conditions_details = st.text_input("If yes, please specify:")

# Plan for Postoperative Care
postoperative_care = st.text_input("Plan for Postoperative Care (e.g., early mobilization, specific diet)")

# Difficulty of Planned Surgery
surgery_difficulty = st.selectbox("Rate the difficulty of the planned surgery", ["Low", "Medium", "High"], index=None)

# Submit Button
if st.button("Submit"):
    # Collecting form data
    form_data = {
        "surgery_type": surgery_type,
        "duration": duration,
        "emergency": emergency,
        "intervention_extent": intervention_extent,
        "anti_adhesion_barriers": anti_adhesion_barriers,
        "blood_loss": blood_loss,
        "pre_existing_adhesions": pre_existing_adhesions,
        "previous_area_surgeries": previous_area_surgeries,
        "bmi": bmi,
        "medications_influence_adhesions": medications_influence_adhesions,
        "medication_details": medication_details if medications_influence_adhesions == "Yes" else None,
        "surgeon_experience": surgeon_experience,
        "anticipated_complications": anticipated_complications,
        "co_morbid_conditions": co_morbid_conditions,
        "conditions_details": conditions_details if co_morbid_conditions == "Yes" else None,
        "postoperative_care": postoperative_care,
        "surgery_difficulty": surgery_difficulty
    }
    
    # Sending POST request
    response = requests.post("https://your-api-endpoint.com/submit", json=form_data)
    
    if response.status_code == 200:
        st.success("Form submitted successfully!")
    else:
        st.error(f"Failed to submit form. Status code: {response.status_code}")

    # Display Summary
    st.write("### Summary of Your Responses")
    st.write(f"Type of Surgery Planned: {surgery_type}")
    st.write(f"Estimated Duration of Surgery: {duration} hours")
    st.write(f"Emergency Surgery: {emergency}")
    st.write(f"Extent of Surgical Intervention: {intervention_extent}")
    st.write(f"Planned Use of Anti-Adhesion Barriers: {anti_adhesion_barriers}")
    st.write(f"Expected Blood Loss: {blood_loss} ml")
    st.write(f"Pre-existing Adhesions Identified: {pre_existing_adhesions}")
    st.write(f"Previous Surgeries in the Same Area: {previous_area_surgeries}")
    st.write(f"Patient's BMI: {bmi}")
    
    if medications_influence_adhesions == "Yes":
        st.write(f"Medications Influencing Adhesion Formation: {medication_details}")
    else:
        st.write("Medications Influencing Adhesion Formation: No")
    
    st.write(f"Surgeon's Experience Level: {surgeon_experience}")
    st.write(f"Intraoperative Complications Anticipated: {anticipated_complications}")
    
    if co_morbid_conditions == "Yes":
        st.write(f"Co-morbid Conditions Affecting Healing: {conditions_details}")
    else:
        st.write("Co-morbid Conditions Affecting Healing: No")
    
    st.write(f"Plan for Postoperative Care: {postoperative_care}")
    st.write(f"Difficulty of Planned Surgery: {surgery_difficulty}")
