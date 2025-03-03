import streamlit as st
import os
from datetime import date
from langchain_core.messages import AIMessage, HumanMessage

from src.langgraphagenticai.ui.uiconfig import Config

class LoadStreamlitUI:
    def __init__(self):
        self.congig = Config()
        self.llm_options = self.config.get_llm_option()
        self.usecase_options = self.config.get_usecase_options()
        self.groq_model_options = self.config.get_groq_model_options()
        self.page_title = self.config.get_page_title()