import streamlit as st
import os
from datetime import date
from langchain_core.messages import AIMessage, HumanMessage

from src.langgraphagenticai.ui.uiconfig import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}
        self.llm_options = self.config.get_llm_options()
        self.usecase_options = self.config.get_usecase_options()
        self.groq_model_options = self.config.get_groq_model_options()
        self.page_title = self.config.get_page_title()

    def initialize_session(self):
        return {
            "current_step": "requirements",
            "requirements": "",
            "user_stories": "",
            "po_feddback": "",
            "generated_code": "",
            "review_feedback": "",
            "decision": None
        }
    
    def load_streamlit_ui(self):
        st.set_page_config(page_title= "🤖" + self.page_title, layout="wide")
        st.header("🤖 " + self.page_title)
        st.session_state.timeFrame = ''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False
    
        with st.sidebar:
            # Get options from config
            llm_options = self.llm_options
            usecase_options = self.usecase_options

            # LLM Selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == "Groq":
                # Model selection 
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", self.groq_model_options)
                # API Key Input
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("Enter GROQ API Key.", type="password")

                # Validate the API Key 
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter the GROQ API Key to Proceed.  Don't have? refere: https://console.groq.com/keys")

            # Usecase Selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecase", usecase_options)

            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()
            # self.render_requirements() # Loads the right side of the UI

        return self.user_controls
    
    def render_requirements(self):
        st.markdown("## Requirements Submission")
        st.session_state.state["requirements"] = st.text_area(
            "Enter Requirements:", 
            height= 200, 
            key="req_input"
        )
        if st.button("Submit Requirements", key = "submit_req"):
            st.session_state.state["current_step"] = "generate_user_stories"
            st.session_state.IsSDLC = True     
    



