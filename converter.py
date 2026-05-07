import streamlit as st

st.title("Currency Converter App")

amount = st.number_input("Enter amount", min_value=0.0, format="%.2f")

option = st.selectbox(
    "Select Conversion",
    ("INR to USD", "USD to INR", "INR to EUR")
)

if st.button("Convert"):

    if option == "INR to USD":
        result = amount * 0.012

    elif option == "USD to INR":
        result = amount * 83.0

    elif option == "INR to EUR":
        result = amount * 0.011

    st.success(f"Converted Amount: {result:.2f}")