import streamlit as st
import google.generativeai as genai

st.title("🎈 My new app")

genai.configure(api_key="AIzaSyA262NFuT3JAtvLAdL6UfVTKPEGOtEr3cc")

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_response(input_text):
  response = model.generate_content(input_text)
  st.write(response)

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if submitted:
    generate_response(text)
