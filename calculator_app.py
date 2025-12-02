import streamlit as st
from operations import add, subtract, multiply, divide

def main():
    st.title("Simple Calculator")

    st.write("Enter two numbers and select an operation.")

    col1, col2 = st.columns(2)
    with col1:
        number1 = st.number_input("First Number", value=0.0, key="number1")
    with col2:
        number2 = st.number_input("Second Number", value=0.0, key="number2")

    operation = st.selectbox(
        "Select Operation",
        ("Add", "Subtract", "Multiply", "Divide"),
        key="operation"
    )

    result = None
    error_message = None

    if st.button("Calculate", key="calculate_button"):
        try:
            if operation == "Add":
                result = add(number1, number2)
            elif operation == "Subtract":
                result = subtract(number1, number2)
            elif operation == "Multiply":
                result = multiply(number1, number2)
            elif operation == "Divide":
                result = divide(number1, number2)
        except ValueError as e:
            error_message = str(e)

    if error_message:
        st.error(f"Error: {error_message}")
    elif result is not None:
        st.success(f"Result: {result}")

if __name__ == "__main__":
    main()

