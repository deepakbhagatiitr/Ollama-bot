import streamlit as st
from langchain_ollama import ChatOllama
import time

# Title and Introduction
st.title("💬 Engage with Ollama and Langchain!")  # Title indicating interaction with the model
st.write("Welcome to this interactive chat application, leveraging the capabilities of Ollama and Langchain. Please feel free to ask your questions, and receive prompt and informative replies!")

# Form to collect user input
with st.form("llm-form"):  # Create a form for user input
    text = st.text_area("Type your message below:", placeholder="Enter your question or prompt...")  # Text area for user input
    submit = st.form_submit_button("Submit")  # Button to submit the form

# Function to generate responses from the model
def generate_response(input_text):
    # Initialize the ChatOllama model with the specified model and base URL
    model = ChatOllama(model="llama3.2:3b", base_url="http://localhost:11434/")
    start_time = time.time()  # Start timing the response generation
    try:
        # Invoke the model with the user input and get the response
        response = model.invoke(input_text)
        elapsed_time = time.time() - start_time  # Calculate elapsed time for the response
        # Check if the response takes longer than expected (10 seconds)
        if elapsed_time > 10:
            return "The response is taking longer than expected. Please try again later."
        return response.content  # Return the content of the response
    except Exception as e:
        return f"An error occurred: {str(e)}"  # Return error message if an exception occurs

# Initialize chat history if not already in session state
if "chat_history" not in st.session_state:  # Check if 'chat_history' is already in session state
    st.session_state['chat_history'] = []  # Initialize an empty chat history list

# Handle form submission
if submit and text:  # Check if the form is submitted and text is provided
    with st.spinner("Generating response..."):  # Show a spinner while generating the response
        response = generate_response(text)  # Generate the response using the input text
        # Store the conversation in session state for future reference
        st.session_state['chat_history'].append({"user": text, "ollama": response})
        # Display the assistant's response
        st.write(f"**🤖 Assistant**: {response}")  # More professional emoji for assistant

# Display chat history in reverse order (latest messages first)
st.write("## Conversation History")  # Section header for chat history
if st.session_state['chat_history']:  # Check if there are any chat history records
    for chat in reversed(st.session_state['chat_history']):  # Loop through chat history in reverse order
        st.write(f"**👤 User**: {chat['user']}")  # Display user messages
        st.write(f"**🤖 Assistant**: {chat['ollama']}")  # Display assistant responses with a more professional tone
        st.write("---")  # Separator between messages
else:
    st.write("Begin a conversation to see the chat history displayed here!")  # Message if no chat history exists
