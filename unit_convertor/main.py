import streamlit as st

# Conversion logic
def convert_units(value, from_unit, to_unit, category):
    if category == "Length":
        factors = {
            "meters": 1,
            "kilometers": 1000,
            "miles": 1609.34,
            "feet": 0.3048,
        }
        return value * factors[from_unit] / factors[to_unit]

    elif category == "Weight":
        factors = {
            "grams": 1,
            "kilograms": 1000,
            "pounds": 453.592,
            "ounces": 28.3495,
        }
        return value * factors[from_unit] / factors[to_unit]

    elif category == "Temperature":
        if from_unit == to_unit:
            return value
        if from_unit == "Celsius":
            return (value * 9/5) + 32 if to_unit == "Fahrenheit" else value + 273.15
        elif from_unit == "Fahrenheit":
            celsius = (value - 32) * 5/9
            return celsius if to_unit == "Celsius" else celsius + 273.15
        elif from_unit == "Kelvin":
            return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

    elif category == "Speed":
        factors = {
            "m/s": 1,
            "km/h": 3.6,
            "mph": 0.44704,
        }
        return value * factors[from_unit] / factors[to_unit]


# UI
st.title("🔄 Unit Converter")
st.subheader("Convert values between common units")

category = st.selectbox("Select a category", ["Length", "Weight", "Temperature", "Speed"])

units = {
    "Length": ["meters", "kilometers", "miles", "feet"],
    "Weight": ["grams", "kilograms", "pounds", "ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Speed": ["m/s", "km/h", "mph"],
}

from_unit = st.selectbox("From", units[category])
to_unit = st.selectbox("To", units[category])
value = st.number_input("Enter value", format="%.4f")

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
