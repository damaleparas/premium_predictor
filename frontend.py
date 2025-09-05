import streamlit as st
import pandas as pd
import requests

# --- 1. FastAPI Endpoint URL ---
# Replace with the actual URL of your running FastAPI server
API_ENDPOINT = "https://premium-predictor-zwiw.onrender.com//predict"

# --- 2. Streamlit UI Components ---
st.set_page_config(page_title="Insurance Premium Predictor", layout="centered")

# Main page title and description
st.title("Insurance Premium Prediction App (API-based)")
st.markdown("This application predicts your potential insurance premium by communicating with a FastAPI backend.")

# --- 3. User Input Section (in sidebar for cleaner layout) ---
st.sidebar.header("User Input Features")

def user_input_features():
    """Collects user input from the sidebar widgets."""
    age = st.sidebar.slider("Age", 18, 100, 30)
    sex_option = st.sidebar.selectbox("Sex", ("male", "female"))
    bmi = st.sidebar.slider("BMI", 10.0, 50.0, 25.0, 0.1)
    children = st.sidebar.slider("Number of Children", 0, 10, 0)
    smoker_option = st.sidebar.selectbox("Smoker", ("yes", "no"))
    region_option = st.sidebar.selectbox("Region", ("northeast", "northwest", "southeast", "southwest"))

    # Return a dictionary that matches the Pydantic model
    data = {
        'age': age,
        'sex': sex_option,
        'bmi': bmi,
        'children': children,
        'smoker': smoker_option,
        'region': region_option
    }
    return data

# Get the user input dictionary
user_data = user_input_features()

# Display the input parameters
st.subheader("Your Input Parameters")
st.json(user_data)

# --- 4. Prediction and Output via API Call ---
# Create a button to trigger the prediction
if st.button("Predict Premium"):
    try:
        # Make a POST request to the FastAPI endpoint
        response = requests.post(API_ENDPOINT, json=user_data)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the JSON response
        prediction_data = response.json()
        prediction = prediction_data.get("predicted forecast charges")

        # Format the output with currency
        if prediction is not None:
            formatted_prediction = f"${prediction:,.2f}"
            st.subheader("Prediction Result")
            st.success(f"The predicted insurance premium is: **{formatted_prediction}**")
        else:
            st.error("Prediction data not found in the API response.")

    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while connecting to the API: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

    # --- 5. Calculate and Display Risk Factor ---
    # The risk factor logic is now in the Streamlit app itself for display purposes
    st.subheader("Risk Factor Assessment")
    
    risk_factor = ""
    if user_data['bmi'] > 35.0 and user_data['smoker'] == "yes":
        risk_factor = "high"
    elif user_data['smoker'] == "yes" and user_data['bmi'] <= 35.0:
        risk_factor = "medium"
    elif user_data['smoker'] == "no":
        risk_factor = "low"
    
    if risk_factor == "high":
        st.error(f"Your calculated risk factor is: **{risk_factor.upper()}**")
    elif risk_factor == "medium":
        st.warning(f"Your calculated risk factor is: **{risk_factor.upper()}**")
    else:
        st.info(f"Your calculated risk factor is: **{risk_factor.upper()}**")
