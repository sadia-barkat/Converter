import streamlit as st

def convert_length(value, from_unit, to_unit):
    length_units = {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "inches": 39.3701,
        "feet": 3.28084,
        "yards": 1.09361,
        "miles": 0.000621371
    }
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15)
    if from_unit == "Fahrenheit":
        return ((value - 32) * 5/9) if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15)
    if from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32)

def main():
    st.markdown("""<h1 style='color: #ff5733; text-align: center;'>🌟 Unit Converter by Sadia 🌟</h1>""", unsafe_allow_html=True)
    
    conversion_type = st.selectbox("⚙️ Select Quantity", ["Length", "Temperature"], format_func=lambda x: f"🌡️ {x}" if x == "Temperature" else f"📏 {x}", help="Choose what you want to convert")
    
    st.markdown("""<hr style='border: 2px solid #3498db;'>""", unsafe_allow_html=True)
    
    value = st.number_input("🔢 Enter Value", min_value=0.0, step=0.1, help="Input the value you want to convert")
    
    if conversion_type == "Length":
        from_unit = st.selectbox("📌 From Unit", ["meters", "kilometers", "centimeters", "millimeters", "inches", "feet", "yards", "miles"], help="Select the unit to convert from")
        to_unit = st.selectbox("🎯 To Unit", ["meters", "kilometers", "centimeters", "millimeters", "inches", "feet", "yards", "miles"], help="Select the unit to convert to")
        if st.button("🚀 Convert", help="Click to convert the value"):
            result = convert_length(value, from_unit, to_unit)
            st.success(f"✅ {value} {from_unit} is equal to {result:.4f} {to_unit}", icon="🎉")
    
    elif conversion_type == "Temperature":
        from_unit = st.selectbox("🌡️ From Unit", ["Celsius", "Fahrenheit", "Kelvin"], help="Select the temperature unit to convert from")
        to_unit = st.selectbox("🔥 To Unit", ["Celsius", "Fahrenheit", "Kelvin"], help="Select the temperature unit to convert to")
        if st.button("⚡ Convert", help="Click to convert the value"):
            result = convert_temperature(value, from_unit, to_unit)
            st.success(f"<p style='color: #e74c3c; font-size: 20px;'>🔥 {value} {from_unit} is <b>{result:.2f}</b> {to_unit}</p>", icon="🌟")
    
if __name__ == "__main__":
    main()
