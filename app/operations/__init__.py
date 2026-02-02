def addition(a: float, b: float) -> float:

    # Add a and b
    return a + b

def subtraction(a: float, b: float) -> float:

    # Subtract a and b
    return a - b

def multiplication(a: float, b: float) -> float:

    # Multiply a and b
    return a * b

def division(a: float, b: float) -> float:

    # Divide a by b. Raise an error if b is zero.
    if b == 0:
        raise ValueError('Division by zero is not allowed.')

    return a / b
