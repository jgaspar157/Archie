import streamlit as st
import numpy as np

# Function to analyze the sequence
def analyze_sequence(sequence):
    n = len(sequence)
    if n < 2:
        return "The sequence is too short to identify a pattern."

    # Convert sequence to NumPy array
    sequence = np.array(sequence)

    # Check for arithmetic sequence
    diffs = np.diff(sequence)
    if np.all(diffs == diffs[0]):
        return f"Arithmetic sequence with a common difference of {diffs[0]}."

    # Check for geometric sequence
    try:
        ratios = sequence[1:] / sequence[:-1]
        if np.all(ratios == ratios[0]):
            return f"Geometric sequence with a common ratio of {ratios[0]}."
    except ZeroDivisionError:
        return "Division by zero encountered while checking for a geometric sequence."

    # Check for Fibonacci-like sequence
    is_fibonacci = True
    for i in range(2, n):
        if sequence[i] != sequence[i - 1] + sequence[i - 2]:
            is_fibonacci = False
            break
    if is_fibonacci:
        return "Fibonacci-like sequence."

    # Check for squares
    if np.all(np.sqrt(sequence) % 1 == 0):
        return "Sequence of perfect squares."

    # Check for cubes
    if np.all(np.cbrt(sequence) % 1 == 0):
        return "Sequence of perfect cubes."

    # If no pattern is found
    return "No simple pattern recognized. It may be a complex or custom pattern."

# Streamlit app
st.title("Number Pattern Analyzer")  # Fixed: Added 'st.' prefix

# Input field for the user
sequence_input = st.text_input("Enter a sequence of numbers (comma-separated):")

if sequence_input:
    try:
        # Convert input to a list of numbers
        sequence = list(map(float, sequence_input.split(',')))
        
        # Analyze the sequence
        result = analyze_sequence(sequence)
        
        # Display the result
        st.write(f"Input Sequence: {sequence}")
        st.write(f"Pattern Detected: {result}")
    except ValueError:
        st.error("Please enter a valid sequence of numbers separated by commas.")
