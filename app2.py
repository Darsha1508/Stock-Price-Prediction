import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("xgboost_model.pkl")

# Streamlit UI
st.markdown('<h1 style="color: MediumSeaGreen;">St💰ck Price Predictio📈 using XGBoost</h1>', unsafe_allow_html=True)

# Stock selection
stock_name = st.radio(
    "Select Stock",
    ("AAPL", "GOOGL", "AMZN", "MSFT", "TSLA")
)

st.write(f"You selected: {stock_name}")

# Input fields
col1, col2 = st.columns(2)
with col1:
    prev_close = st.number_input("Previous Close Price", value=0.0)
    open_price = st.number_input("Open Price", value=0.0)
    high_price = st.number_input("High Price", value=0.0)
    low_price = st.number_input("Low Price", value=0.0)
with col2:
    last_price = st.number_input("Last Price", value=0.0)
    close_price = st.number_input("Close Price", value=0.0)
    volume = st.number_input("Volume", value=0)

# Predict button
if st.button("Predict VWAP"):
    if low_price > high_price:
        st.error("Invalid Inputs!!! High price cannot be less than Low price.")
    elif low_price > close_price:
        st.error("Invalid Inputs!!! Close price cannot be less than Low price.")
    #elif open_price < close_price:
        #st.error("Invalid Inputs!!! Open price cannot be less than Close price.")
    else:
        # Prepare input data
        input_data = np.array([[prev_close, open_price, high_price, low_price, last_price, close_price, volume]])
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Display result
        st.success(f"Predicted VWAP for {stock_name}: {prediction[0]:.2f}")
        st.success("✅ VWAP calculated successfully! Your result is displayed above.")
