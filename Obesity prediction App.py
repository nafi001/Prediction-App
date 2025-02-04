import streamlit as st
import pandas as pd
import joblib

# Correct the filename and path
pipeline = joblib.load('NeuralNetwork_pipeline.joblib')

# Streamlit form for user input
st.title("Obesity Prediction")
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=0, max_value=100)
height = st.number_input("Height (meterstreamlit run app.py)", min_value=0.5, max_value=2.5)
weight = st.number_input("Weight (kg)", min_value=10, max_value=200)
family_history = st.selectbox("Family history with overweight", ["yes", "no"])
favc = st.selectbox("Do you eat high caloric food frequently?", ["yes", "no"])
fcvc = st.slider("Do you usually eat vegetables in your meals?", 0, 3)
ncp = st.slider("How many main meals do you have daily?", 1, 10)
caec = st.selectbox("Do you eat any food between meals?", ["Always", "Frequently", "Sometimes", "no"])
smoke = st.selectbox("Do you smoke?", ["yes", "no"])
ch2o = st.slider("How much water do you drink daily? (liters)", 0.0, 10.0)
scc = st.selectbox("Do you monitor the calories you eat daily?", ["yes", "no"])
faf = st.slider("How often do you have physical activity? (hours per day)", 0.0, 24.0)
tue = st.slider("How much time do you use technological devices daily? (hours per day)", 0, 24)
calc = st.selectbox("How often do you drink alcohol?", ["Always", "Frequently", "Sometimes", "no"])
mtrans = st.selectbox("Which transportation do you usually use?", ["Automobile", "Bike", "Motorbike", "Public_Transportation", "Walking"])

# Create user input dictionary
user_input = {
    'Gender': gender,
    'Age': age,
    'Height': height,
    'Weight': weight,
    'family_history_with_overweight': family_history,
    'FAVC': favc,
    'FCVC': fcvc,
    'NCP': ncp,
    'CAEC': caec,
    'SMOKE': smoke,
    'CH2O': ch2o,
    'SCC': scc,
    'FAF': faf,
    'TUE': tue,
    'CALC': calc,
    'MTRANS': mtrans
}

# Convert user input to DataFrame
user_df = pd.DataFrame([user_input])

# Make prediction
prediction = pipeline.predict(user_df)

# Display the prediction
st.write("Predicted Obesity Level:", prediction[0])
