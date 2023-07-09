import streamlit as st
import sys
import os
from src.TextSummarization.pipeline.prediction import PredictionPipeline

if 'output' not in st.session_state:
    st.session_state.output = ""

def predict(text):
    try:
        obj = PredictionPipeline()
        output = obj.predict(text)
        return output
    except Exception as e:
        raise e

st.write("# Text Summarizer")
st.write("""
AI-Based Tool to Summarize Text using NLP techniques
""")
         
user_input = st.text_area(label="Enter Text to Summarize :pencil:", value="", height=20)
button = st.button(label="Summarize")
if button: 
    st.session_state.output = "Loading..."
    output = predict(user_input)
    st.session_state.output = output

st.write("Output: ", st.session_state.output)


# button1 = st.button(label="Counter")
# if ('count' not in st.session_state) :
#     st.session_state.count = 0

# if button1:
#     st.session_state.count += 1

# st.write("Count: ", st.session_state.count)


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 