import streamlit as st

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



st.title("Vaccine Misinformation Chatbot")

user_input = st.text_input("Enter misinformation claim:")

if user_input:
    corrected_text = generate_response(user_input)
    st.write("Corrected Response:", corrected_text)
