import streamlit as st

# Title of the app
st.title("Simple Streamlit Application")

# Prompt user for their name
name = st.text_input("Enter your name:")

# Display a greeting message when user enters a name
if name:
    st.write(f"Hello, {name}! Welcome to the Streamlit app!")
else:
    st.write("Please enter your name above.")
