import streamlit as st
import string

st.title("Advanced Word & Character Counter")

# User input text area
text = st.text_area("Enter your text here:", height=200)

if text:  # Only process if text is entered
    char_count = len(text)  # Total characters
    word_count = len(text.split())  # Total words

    # Counting small letters, capital letters, special characters, and spaces
    small_letters = sum(1 for char in text if char.islower())
    capital_letters = sum(1 for char in text if char.isupper())
    special_chars = sum(1 for char in text if char in string.punctuation)
    white_spaces = sum(1 for char in text if char.isspace())

    # Displaying results
    st.write(f"**Total Characters:** {char_count}")
    st.write(f"**Total Words:** {word_count}")
    st.write(f"**Small Letters:** {small_letters}")
    st.write(f"**Capital Letters:** {capital_letters}")
    st.write(f"**Special Characters:** {special_chars}")
    st.write(f"**White Spaces:** {white_spaces}")

else:
    st.write("Start typing to see the counts!")

 
