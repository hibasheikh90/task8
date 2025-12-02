def add(num1: float, num2: float) -> float:
    """Adds two numbers and returns the sum."""
    return num1 + num2

def subtract(num1: float, num2: float) -> float:
    """Subtracts the second number from the first and returns the difference."""
    return num1 - num2

def multiply(num1: float, num2: float) -> float:
    """Multiplies two numbers and returns the product."""
    return num1 * num2

def divide(num1: float, num2: float) -> float:
    """Divides the first number by the second and returns the quotient.
    Raises ValueError if division by zero is attempted.
    """
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2
