# Q&A Chatbot
from langchain_openai import OpenAI
import streamlit as st
#import os
#from dotenv import load_dotenv
#load_dotenv()
#api_key = os.environ['OPENAI_API_KEY']
# Function to create OpenAI model & get response
# openai_api_key=os.getenv("OPENAI_API_KEY")
def get_openai_response(question):
    llm = OpenAI(openai_api_key=OPENAI_API_KEY,
                 model_name='gpt-3.5-turbo-instruct', 
                 temperature=0.5)
    response = llm(question)
    return response

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

# Get user input
user_input = st.text_input("Input:", key="user_input")

# Button to submit the input
submit = st.button("Submit")

# If submit button is clicked
if submit and user_input:
    response = get_openai_response(user_input)
    st.subheader("The response is")
    st.write(response)