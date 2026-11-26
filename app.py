import streamlit as st
from groq import Groq

st.set_page_config(page_title='AI Iterview Assistant',layout='centered')
st.title('AI Interview Assistant')
st.caption('Practice interview with AI-generated questions and constructive')
st.caption("harshitha")
st.write("Department of AIDS")

try:
  client=Groq(api_key=st.secrets['GROQ_API_KEY'])
  st.write("API connection successful")
except (KeyError, FileNotFoundError):
  st.error('GROQ_API_KEY is missing.')
  st.stop() 

st.title("AI Interview Assistant")
role = st.selectbox("Select Job Role",[
  "Python Developer",
  "Java Developer",
  "Data Analyst",
  "Machine Learning Engineer",
  "Software Engineer",
  "HR Executive"
])
