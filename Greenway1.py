import streamlit as st
import spacy

# Load the English language model from spaCy
nlp = spacy.load("en_core_web_sm")

# Define the categories to classify the words
categories = [
    "Noun", "Verb", "Adjective", "Adverb", "Pronoun", "Preposition", "Conjunction", "Interjection",
    "Proper Noun", "Determiner", "Auxiliary Verb", "Cardinal Number", "Ordinal Number", "Quantifier", 
    "Particle", "Phrasal Verb", "Possessive Pronoun", "Reflexive Pronoun", "Relative Pronoun"
]

# Function to get the category of a word
def get_word_category(word):
    doc = nlp(word)
    if doc:
        # Get the POS tag of the word
        pos_tag = doc[0].pos_
        # Map POS tags to categories
        if pos_tag == "NOUN":
            return "Noun"
        elif pos_tag == "VERB":
            return "Verb"
        elif pos_tag == "ADJ":
            return "Adjective"
        elif pos_tag == "ADV":
            return "Adverb"
        elif pos_tag == "PRON":
            return "Pronoun"
        elif pos_tag == "ADP":
            return "Preposition"
        elif pos_tag == "CCONJ":
            return "Conjunction"
        elif pos_tag == "INTJ":
            return "Interjection"
        elif pos_tag == "PROPN":
            return "Proper Noun"
        elif pos_tag == "DET":
            return "Determiner"
        elif pos_tag == "AUX":
            return "Auxiliary Verb"
        elif pos_tag == "NUM":
            if word.isdigit():
                return "Cardinal Number"
            else:
                return "Ordinal Number"
        elif pos_tag == "PART":
            return "Particle"
        else:
            return "Unknown"
    return "Unknown"

# Streamlit app layout
st.title("Word Category Identifier")

# Input field for the word
word_input = st.text_input("Enter a word:")

# Button to trigger the categorization
if st.button("Identify Category"):
    if word_input:
        category = get_word_category(word_input)
        st.write(f"The word '{word_input}' is categorized as: {category}")
    else:
        st.write("Please enter a word to identify its category.")

# Display the list of available categories
st.subheader("Available Categories")
st.write(categories)
