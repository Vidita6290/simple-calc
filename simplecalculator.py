import streamlit as st

st.title("Simple Calculator")
num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")
operation = st.selectbox("Operation:",["Add","Substract","Multiplication","Division"])
result = None
if st.button("Submit"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Substract":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        result = num1 / num2

st.write(f"The result is:{result}")