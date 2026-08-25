import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details to predict whether the transaction is fraudulent.")

# Input fields
time = st.number_input("Time", min_value=0.0, value=0.0)
amount = st.number_input("Amount", min_value=0.0, value=100.0)

st.subheader("Transaction Features")

v_features = []

for i in range(1, 29):
    value = st.number_input(f"V{i}", value=0.0)
    v_features.append(value)

# Prediction
if st.button("Predict"):

    input_data = pd.DataFrame(
        [[time] + v_features + [amount]],
        columns=["Time"] + [f"V{i}" for i in range(1, 29)] + ["Amount"]
    )

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction appears to be Legitimate.")