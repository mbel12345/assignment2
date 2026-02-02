import sys

from io import StringIO

from app.calculator import calculator

def run_calc(monkeypatch, capsys, user_inputs):

    # Simulate reading input from user, and return the output from the calculator app.

    inputs = iter(user_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    for user_input in user_inputs:
        monkeypatch.setattr(sys, 'stdin', StringIO(user_input))

    calculator()

    captured = capsys.readouterr().out
    return captured

# Tests for valid inputs

def test_addition(monkeypatch, capsys):

    # Test addition for REPL calculator

    inputs = ['add 2 5', 'exit']
    output = run_calc(monkeypatch, capsys, inputs)
    assert 'Result: 7.0' in output

def test_subtraction(monkeypatch, capsys):

    # Test subtraction for REPL calculator

    inputs = ['subtract 9 5', 'exit']
    output = run_calc(monkeypatch, capsys, inputs)
    assert 'Result: 4.0' in output

def test_multiplication(monkeypatch, capsys):

    # Test multiplication for REPL calculator

    inputs = ['multiply 3 5', 'exit']
    output = run_calc(monkeypatch, capsys, inputs)
    assert 'Result: 15.0' in output

def test_division(monkeypatch, capsys):

    # Test division for REPL calculator

    inputs = ['divide 6 2', 'exit']
    output = run_calc(monkeypatch, capsys, inputs)
    assert 'Result: 3.0' in output

# Tests for invalid inputs

def test_invalid_operation(monkeypatch, capsys):

    # Test invalid operation for REPL calculator

    inputs = ['longdivide 9 3', 'exit']
    output = run_calc(monkeypatch, capsys, inputs)
    assert 'Unknown operation' in output

def test_too_many_inputs(monkeypatch, capsys):

    # Test sending too may inputs to the REPL calculator
    inputs = ['add 3 4 extra-arg', 'exit']
    output = run_calc(monkeypatch, capsys, inputs)
    assert 'Invalid input. Please follow the format' in output

def test_invalid_input_format(monkeypatch, capsys):

    # Test invalid format for REPL calculator

    inputs = ['add two 7', 'exit']
    output = run_calc(monkeypatch, capsys, inputs)
    assert 'Invalid input. Please follow the format' in output

def test_division_by_zero(monkeypatch, capsys):

    # Test division by 0 for REPL calculator

    inputs = ['divide 8 0', 'exit']
    output = run_calc(monkeypatch, capsys, inputs)
    assert 'Division by zero is not allowed' in output
