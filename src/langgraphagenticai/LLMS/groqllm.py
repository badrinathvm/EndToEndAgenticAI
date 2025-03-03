import streamlit as st
import os
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls = user_controls_input

    def get_llm_model(self):
        """
        Get the LLM model based on the user input.

        Returns:
            str: The LLM model.
        """
        try:
            groq_api_key = self.user_controls["GROQ_API_KEY"]
            selected_groq_model = self.user_controls["selected_groq_model"]
            if groq_api_key == '' and os.environ["GROQ_API_KEY"] == '':
                st.error("Please enter the GROQ API Key to proceed.")

            llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)
            return llm
        except Exception as e:
            raise ValueError(f"Error Occurred with exception: {e}")
