from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

# Ensure the GOOGLE_API_KEY is set in your environment variables
google_api_key = os.getenv('GOOGLE_API_KEY')

# Define the prompt template
prompt_template = "Draft an email on {subject} with a {tone} tone."
email_prompt = PromptTemplate(template=prompt_template, input_variables=['subject', 'tone'])

# Initialize the Google Generative AI model
gemini_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")

# Create the LLMChain
chain = email_prompt | gemini_model

# Streamlit app layout
st.set_page_config(page_title="📧 Email Generator", page_icon="✉️", layout="centered")

# Header with emojis
st.header("📧 Email Generator App by Sreevalli")
st.subheader("✨ This app helps you draft professional emails effortlessly.")

# User input
subject = st.text_input('📝 Enter the subject of the email:', placeholder="e.g., Leave Request, Meeting Invitation")
tone = st.selectbox("🎨 Select the tone:", ["Formal", "Casual", "Friendly", "Persuasive"])

# Generate button with emoji
if st.button('🚀 Generate Email'):
    if subject:
        with st.spinner("⏳ Generating your email..."):
            try:
                # Invoke the chain with user inputs (subject and tone)
                response = chain.invoke({'subject': subject, 'tone': tone})
                st.success("✅ Email generated successfully!")
                st.write(response.content)
            except Exception as e:
                st.error(f"❌ An error occurred: {e}")
    else:
        st.warning("⚠️ Please enter a subject for the email.")
