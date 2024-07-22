import streamlit as st
import requests

st.title("Doctor Questionnaire for Predicting Adhesion Risk")

# Type of Surgery Planned
surgery_type = st.selectbox("Type of Surgery Planned", ["Diagnostic endoscopy", "Therapeutic endoscopy", "Laparoscopic surgery", "Open abdominal surgery", "Other"], index=2)

# Estimated Duration of Surgery (in hours)
duration = st.number_input("Estimated Duration of Surgery (in hours)", value=1.5, min_value=0.0, step=0.1)

# Emergency Surgery
emergency = st.radio("Is the surgery being performed as an emergency?", ["Yes", "No"], index=1)

# Extent of Surgical Intervention
intervention_extent = st.selectbox("Extent of Surgical Intervention", ["Minor", "Moderate", "Extensive"], index=0)

# Planned Use of Anti-Adhesion Barriers
anti_adhesion_barriers = st.radio("Planned Use of Anti-Adhesion Barriers", ["Yes", "No"], index=0)

# Expected Blood Loss (ml)
blood_loss = st.number_input("Expected Blood Loss (ml)", value=15, min_value=0, step=1)

# Presence of Pre-existing Adhesions Identified in Imaging
pre_existing_adhesions = st.radio("Presence of Pre-existing Adhesions Identified in Imaging?", ["Yes", "No"], index=1)

# Previous Surgeries in the Same Area
previous_area_surgeries = st.radio("Previous Surgeries in the Same Area?", ["Yes", "No"], index=0)

# Patient's BMI (Body Mass Index)
bmi = st.number_input("Patient's BMI (Body Mass Index)", value=24.0, min_value=0.0, step=0.1)

# Planned Use of Medications Known to Influence Adhesion Formation
medications_influence_adhesions = st.radio("Any planned use of medications known to influence adhesion formation (e.g., steroids, anticoagulants)?", ["Yes", "No"], index=1)
if medications_influence_adhesions == "Yes":
    medication_details = st.text_input("If yes, please specify:", key="medication_details")

# Surgeon's Experience Level
surgeon_experience = st.selectbox("Surgeon's experience level with the specific procedure", ["Novice", "Intermediate", "Expert"], index=2)

# Intraoperative Complications Anticipated
anticipated_complications = st.radio("Intraoperative Complications Anticipated?", ["Yes", "No"], index=1)

# Presence of Co-morbid Conditions Affecting Healing
co_morbid_conditions = st.radio("Presence of Co-morbid Conditions Affecting Healing?", ["Yes", "No"], index=1)
if co_morbid_conditions == "Yes":
    conditions_details = st.text_input("If yes, please specify:", key="conditions_details")

# Plan for Postoperative Care
postoperative_care = st.text_input("Plan for Postoperative Care (e.g., early mobilization, specific diet)", key="postoperative_care")

# Difficulty of Planned Surgery
surgery_difficulty = st.selectbox("Rate the difficulty of the planned surgery", ["Low", "Medium", "High"], index=1)

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
    response = requests.post("https://hook.eu2.make.com/lxxwvlmie4yq4834xpq4pur3yjupct9b", json=form_data)
    
    if response.status_code == 200:
        st.success("Form submitted successfully!")
    else:
        st.error(f"Failed to submit form. Status code: {response.status_code}")

        # Display Summary
    summary_patient = f"""
    ### Summary of Patients' Responses
    - **Age:** 27
    - **Gender:** Female
    - **Height:** 168.0 cm
    - **Weight:** 58.0 kg
    - **Previous Abdominal Surgeries:** No
    - **Smokes:** No
    - **Consumes Alcohol:** Yes, 2 units per week
    - **Chronic Diseases:** No
    - **Family History of Adhesions:** No
    - **Abdominal Infection:** No
    - **Medication:** No
    - **Physical Activity Level:** Moderately active
    """


    summary = f"""
    ### Summary of Doctors' Responses
    - **Type of Surgery Planned:** {surgery_type}
    - **Estimated Duration of Surgery:** {duration} hours
    - **Emergency Surgery:** {emergency}
    - **Extent of Surgical Intervention:** {intervention_extent}
    - **Planned Use of Anti-Adhesion Barriers:** {anti_adhesion_barriers}
    - **Expected Blood Loss:** {blood_loss} ml
    - **Pre-existing Adhesions Identified:** {pre_existing_adhesions}
    - **Previous Surgeries in the Same Area:** {previous_area_surgeries}
    - **Patient's BMI:** {bmi}
    - **Medications Influencing Adhesion Formation:** {'Yes, ' + medication_details if medications_influence_adhesions == "Yes" else "No"}
    - **Surgeon's Experience Level:** {surgeon_experience}
    - **Intraoperative Complications Anticipated:** {anticipated_complications}
    - **Co-morbid Conditions Affecting Healing:** {'Yes, ' + conditions_details if co_morbid_conditions == "Yes" else "No"}
    - **Plan for Postoperative Care:** {postoperative_care}
    - **Difficulty of Planned Surgery:** {surgery_difficulty}
    """

    st.info(summary_patient)
    st.success(summary)

    st.title("Surgery Risk Evaluation System for Adhesion-Free Endoscopies")

    fixed_value = 74

    # Display the fixed value
    st.write("Risk of Development of Abdominal Adhesions:", fixed_value)

    # Optionally, show a visual representation (like a progress bar)
    st.progress(fixed_value)
    st.write("This prediction highlights the need for heightened vigilance and targeted preventive strategies. The high risk is often associated with factors such as prior abdominal surgeries and a predisposition to inflammatory responses. Recognizing this risk prior to surgery allows doctors to adjust their preventive measures accordingly. Implementing adhesion barriers, employing meticulous surgical techniques to minimize tissue trauma, and planning comprehensive postoperative care focused on reducing inflammation are crucial steps. These measures aim to reduce the likelihood of adhesions, thereby promoting a smoother recovery and minimizing potential complications.")

    image_path = "SHAP.png"

    st.image(image_path, caption='Prediction Explanation', use_column_width=True)


