title("Number Pattern Analyzer")

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
