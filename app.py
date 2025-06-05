import streamlit as st
import joblib
import numpy as np
from PIL import Image
import base64
#@st.experimental_memo
def set_background(img_file):
    with open(img_file, "rb") as img:
     data = img.read()
    return base64.b64encode(data).decode()

image = set_background("bgf.avif")

bg_img = f"""
<style>
[data-testid = "stAppViewContainer"]{{
background-image: url("data:size/jpg;base64,{image}");
background-size: cover;
background-position: centre;
}}

</style>
"""
st.markdown(bg_img, unsafe_allow_html = True)

st.markdown("""
<style>
.stButton>button {
    background-color: #4CAF50;  /* Green background */
    color: white;  /* White text */
    border: none;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    cursor: pointer;
    border-radius: 12px;
    box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.3);
}
.stButton>button:hover {
    background-color: DodgerBlue;  /* Darker green on hover */
}
</style>
""", unsafe_allow_html=True)


# Load the model
model = joblib.load("xgboost_model.pkl")

# Streamlit UI
st.markdown('<h1 style="color: MediumSeaGreen;">St💰ck Price Predictio📈 using XGBoost', unsafe_allow_html=True)

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
    if(low_price>high_price):
        st.error("Invalid Inputs!!! High price cannot be less than Low price ")
    elif (low_price>close_price):
        st.error("Invalid Inputs!!! Close price cannot be less than Low price ")
   ## elif (open_price<close_price):
        ##st.error("Invalid Inputs!!! Open price cannot be less than Close price ")
    else:
        # Prepare input data
        input_data = np.array([[prev_close, open_price, high_price, low_price, last_price, close_price, volume]])
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Display result
        st.success(f"Predicted VWAP: {prediction[0]:.2f}")
        st.success("✅ VWAP calculated successfully! Your result is displayed above.")