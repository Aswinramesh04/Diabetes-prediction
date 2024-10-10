import streamlit as st
import requests  # Import requests to make API calls

# Streamlit app title
st.title('Diabetes Prediction Web App')

# Input fields for user data
Pregnancies = st.text_input('Number of Pregnancies', '0')
Glucose = st.text_input('Glucose Level', '0')
BloodPressure = st.text_input('Blood Pressure value', '0')
SkinThickness = st.text_input('Skin Thickness value', '0')
Insulin = st.text_input('Insulin Level', '0')
BMI = st.text_input('BMI value', '0.0')
DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', '0.0')
Age = st.text_input('Age of the Person', '0')

# Button for prediction
if st.button('Diabetes Test Result'):
    # Creating a dictionary to hold input data
    payload = {
        'Pregnancies': int(Pregnancies),
        'Glucose': float(Glucose),
        'BloodPressure': float(BloodPressure),
        'SkinThickness': float(SkinThickness),
        'Insulin': float(Insulin),
        'BMI': float(BMI),
        'DiabetesPedigreeFunction': float(DiabetesPedigreeFunction),
        'Age': int(Age)
    }

    # Sending the data to FastAPI for prediction
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        
        # Checking the response from the FastAPI app
        if response.status_code == 200:
            diagnosis = response.json()['result']
            st.success(f'The prediction result is: {diagnosis}')
        else:
            st.error(f'Error in prediction: {response.json()}')
    except Exception as e:
        st.error(f'Failed to connect to FastAPI: {e}')
