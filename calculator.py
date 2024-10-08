import streamlit as st


# Title of the app
st.title("Simple Calculator")

# Getting user input for two numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Dropdown menu for selecting the operation
operation = st.selectbox("Select Operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform the calculation based on user input
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."

# Display the result
st.write("Result_W:", result)


