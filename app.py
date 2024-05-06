from dotenv import load_dotenv 
import streamlit as st 
import os 
import google.generativeai as genai 
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Functiom to load Gemini pro model and get response 

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question): 
    response = chat.send_message(question,stream=True)
    return response 



