import streamlit as st
from langchain_ollama import ChatOllama
import time

st.title("💬 Engage with Ollama and Langchain!")
st.write("Welcome to this interactive chat application, leveraging the capabilities of Ollama and Langchain. Please feel free to ask your questions, and receive prompt and informative replies!")

with st.form("llm-form"):
    text = st.text_area("Type your message below:", placeholder="Enter your question or prompt...")
    submit = st.form_submit_button("Submit")

def generate_response(input_text):
    model = ChatOllama(model="llama3.2:3b", base_url="http://localhost:11434/")
    start_time = time.time()
    try:
        response = model.invoke(input_text)
        elapsed_time = time.time() - start_time
        if elapsed_time > 10:
            return "The response is taking longer than expected. Please try again later."
        return response.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

if submit and text:
    with st.spinner("Generating response..."):
        response = generate_response(text)
        st.session_state['chat_history'].append({"user": text, "ollama": response})
        st.write(f"**🤖 Assistant**: {response}")

st.write("## Conversation History")
if st.session_state['chat_history']:
    for chat in reversed(st.session_state['chat_history']):
        st.write(f"**👤 User**: {chat['user']}")
        st.write(f"**🤖 Assistant**: {chat['ollama']}")
        st.write("---")
else:
    st.write("Begin a conversation to see the chat history displayed here!")
