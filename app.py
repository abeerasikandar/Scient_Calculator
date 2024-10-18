import math
import streamlit as st

# Define calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def log(x, base=10):
    if x <= 0:
        return "Error: Logarithm of non-positive number is not defined."
    return math.log(x, base)

def absolute(x):
    return abs(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

# Start the Streamlit app
st.title("🧮 Interactive Scientific Calculator")

# Description
st.markdown("""
This is an **interactive scientific calculator** built using Python and Streamlit. 
You can perform basic arithmetic operations as well as advanced mathematical functions like trigonometry and logarithms. 
Choose an operation from the dropdown, and the result will be displayed in real time as you input values.
""")

# Select operation
operation = st.selectbox(
    "Select the operation you want to perform:",
    ["Addition", "Subtraction", "Multiplication", "Division", 
     "Logarithm", "Absolute", "Sine", "Cosine", "Tangent"]
)

st.write("---")  # Line separator for better UI

# Input for basic operations
if operation in ["Addition", "Subtraction", "Multiplication", "Division"]:
    x = st.number_input(f"Enter the first number for {operation}", value=0.0)
    y = st.number_input(f"Enter the second number for {operation}", value=0.0)

    if operation == "Addition":
        result = add(x, y)
        st.write(f"**Result:** {x} + {y} = {result}")
    elif operation == "Subtraction":
        result = subtract(x, y)
        st.write(f"**Result:** {x} - {y} = {result}")
    elif operation == "Multiplication":
        result = multiply(x, y)
        st.write(f"**Result:** {x} * {y} = {result}")
    elif operation == "Division":
        result = divide(x, y)
        st.write(f"**Result:** {x} / {y} = {result}")

# Logarithm
elif operation == "Logarithm":
    x = st.number_input("Enter the number for logarithm", value=1.0)
    base = st.number_input("Enter base (default is 10)", value=10.0)
    
    result = log(x, base)
    st.write(f"**Result:** log({x}) base {base} = {result}")

# Absolute
elif operation == "Absolute":
    x = st.number_input("Enter the number to find the absolute value", value=0.0)

    result = absolute(x)
    st.write(f"**Result:** |{x}| = {result}")

# Trigonometric functions
elif operation == "Sine":
    x = st.slider("Enter the angle in degrees for sine", min_value=-360.0, max_value=360.0, value=0.0)

    result = sine(x)
    st.write(f"**Result:** sin({x}) = {result}")

elif operation == "Cosine":
    x = st.slider("Enter the angle in degrees for cosine", min_value=-360.0, max_value=360.0, value=0.0)

    result = cosine(x)
    st.write(f"**Result:** cos({x}) = {result}")

elif operation == "Tangent":
    x = st.slider("Enter the angle in degrees for tangent", min_value=-360.0, max_value=360.0, value=0.0)

    result = tangent(x)
    st.write(f"**Result:** tan({x}) = {result}")

st.write("---")  # Line separator for better UI
st.markdown("""
Made with ❤️ using **Python** and **Streamlit**. 
You can enhance this calculator further by adding more complex functions and refining the UI!
""")
