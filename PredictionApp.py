aaaa
import streamlit as st
import pandas as pd
import joblib
import pandas as pd
# Load the trained model
pipeline = joblib.load('NeuralNetwork_pipeline.joblib')

# Set page configuration
st.set_page_config(page_title="Obesity Prediction", page_icon="🩺", layout="centered")

st.title("🏥 Obesity Prediction System")
st.markdown("### Provide your details to predict obesity level.")

# Custom CSS for improved styling
st.markdown("""
    <style>
        div.stSlider > div[data-baseweb="slider"] > div > div {
            
        }
        .stApp {
           
        }
        .title {
            
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# User Input Form
with st.form("user_input_form"):
    st.subheader("👤 Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        age = st.number_input("Age", min_value=0, max_value=100)
    with col2:
        height = st.number_input("Height (meter)", min_value=0.5, max_value=2.5)
        weight = st.number_input("Weight (kg)", min_value=10, max_value=200)

    st.subheader("🍽️ Lifestyle & Habits")
    col1, col2 = st.columns(2)
    with col1:
        family_history = st.radio("Family history of overweight?", ["yes", "no"])
        favc = st.radio("Eat high caloric food frequently?", ["yes", "no"])
        fcvc = st.slider("Vegetable consumption (0: Low - 3: High)", 0, 3)
        ncp = st.slider("Main meals per day", 1, 10)
    with col2:
        caec = st.selectbox("Snack frequency", ["Always", "Frequently", "Sometimes", "No"])
        smoke = st.radio("Do you smoke?", ["yes", "no"])
        ch2o = st.slider("Daily water intake (liters)", 0.0, 10.0)
        scc = st.radio("Monitor calorie intake?", ["yes", "no"])

    st.subheader("🏃 Physical Activity & Tech Usage")
    col1, col2 = st.columns(2)
    with col1:
        faf = st.slider("Physical activity (hours/day)", 0.0, 24.0)
        tue = st.slider("Tech usage (hours/day)", 0, 24)
    with col2:
        calc = st.selectbox("Alcohol consumption", ["Always", "Frequently", "Sometimes", "No"])
        mtrans = st.selectbox("Usual mode of transportation", ["Automobile", "Bike", "Motorbike", "Public Transport", "Walking"])

    # Submit button
    submit = st.form_submit_button("🔍 Predict Obesity Level")

if submit:
    # Convert user input to DataFrame
    user_input = {
        'Gender': gender, 'Age': age, 'Height': height, 'Weight': weight,
        'family_history_with_overweight': family_history, 'FAVC': favc,
        'FCVC': fcvc, 'NCP': ncp, 'CAEC': caec, 'SMOKE': smoke,
        'CH2O': ch2o, 'SCC': scc, 'FAF': faf, 'TUE': tue, 'CALC': calc, 'MTRANS': mtrans
    }
    user_df = pd.DataFrame([user_input])

    # Make prediction
    prediction = pipeline.predict(user_df)[0]

    # Detect Streamlit theme
    theme = st.get_option("theme.base")
    is_dark_mode = theme == "dark"

    # Define colors for both light and dark modes
    color_map = {
        "Insufficient_Weight": "#3498db" if not is_dark_mode else "#85C1E9",
        "Normal_Weight": "#2ecc71" if not is_dark_mode else "#58D68D",
        "Overweight_Level_I": "#f1c40f" if not is_dark_mode else "#F7DC6F",
        "Overweight_Level_II": "#e67e22" if not is_dark_mode else "#F5B041",
        "Obesity_Type_I": "#e74c3c" if not is_dark_mode else "#EC7063",
        "Obesity_Type_II": "#c0392b" if not is_dark_mode else "#D98880",
        "Obesity_Type_III": "#8e44ad" if not is_dark_mode else "#BB8FCE"
    }

    # Display result
    st.subheader("🩺 Prediction Result")
    st.markdown(
        f"<h3 style='color: {color_map.get(prediction, '#FFF' if is_dark_mode else '#000')}; text-align:center;'>{prediction.replace('_', ' ')}</h3>",
        unsafe_allow_html=True
    )
