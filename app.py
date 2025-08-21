import streamlit as st
import requests


def get_perplexity_response(input_text1):
    response=requests.post("http://localhost:8000/highlights/invoke",
                  json={"input":{"subject": input_text1}})
    
    return response.json()["output"]


def get_ollama_response(input_text2):
    response=requests.post("http://localhost:8000/summary/invoke",
                  json={"input":{"subject": input_text2}})

    return response.json()["output"]


# Streamlit framework
input_text1 = st.text_input("Give me a subject to highlight key points")
input_text2 = st.text_input("Give me a subject to summarize")


# Streamlit logic code
if input_text1:
    st.write(get_perplexity_response(input_text1))

if input_text2:
    st.write(get_ollama_response(input_text2))