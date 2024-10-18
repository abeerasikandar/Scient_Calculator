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

# Streamlit app starts here
st.title("Scientific Calculator")

# Select operation
operation = st.selectbox("Select Operation", 
                         ["Addition", "Subtraction", "Multiplication", "Division", 
                          "Logarithm", "Absolute", "Sine", "Cosine", "Tangent"])

# Input for basic operations
if operation in ["Addition", "Subtraction", "Multiplication", "Division"]:
    x = st.number_input("Enter first number", value=0.0)
    y = st.number_input("Enter second number", value=0.0)

    if st.button("Calculate"):
        if operation == "Addition":
            st.write(f"Result: {x} + {y} = {add(x, y)}")
        elif operation == "Subtraction":
            st.write(f"Result: {x} - {y} = {subtract(x, y)}")
        elif operation == "Multiplication":
            st.write(f"Result: {x} * {y} = {multiply(x, y)}")
        elif operation == "Division":
            result = divide(x, y)
            st.write(f"Result: {x} / {y} = {result}")

# Logarithm
elif operation == "Logarithm":
    x = st.number_input("Enter the number", value=1.0)
    base = st.number_input("Enter base (default is 10)", value=10.0)
    
    if st.button("Calculate"):
        result = log(x, base)
        st.write(f"Result: log({x}) base {base} = {result}")

# Absolute
elif operation == "Absolute":
    x = st.number_input("Enter the number", value=0.0)

    if st.button("Calculate"):
        result = absolute(x)
        st.write(f"Result: |{x}| = {result}")

# Trigonometric functions
elif operation == "Sine":
    x = st.number_input("Enter the angle in degrees", value=0.0)

    if st.button("Calculate"):
        result = sine(x)
        st.write(f"Result: sin({x}) = {result}")

elif operation == "Cosine":
    x = st.number_input("Enter the angle in degrees", value=0.0)

    if st.button("Calculate"):
        result = cosine(x)
        st.write(f"Result: cos({x}) = {result}")

elif operation == "Tangent":
    x = st.number_input("Enter the angle in degrees", value=0.0)

    if st.button("Calculate"):
        result = tangent(x)
        st.write(f"Result: tan({x}) = {result}")
