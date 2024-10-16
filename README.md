
# Ollama Chatbot

This project demonstrates how to create a robust chatbot using **Langchain**, **Ollama**, and Facebook's **LLAMA 3.2 (llama3.2:3b)** model. LLAMA 3.2 is a cutting-edge local large language model (LLM) designed for building intelligent chatbot functionalities. The chatbot integrates with **Streamlit** to provide a user-friendly interface for seamless interaction.

## Features

- **Local LLM Setup**: Get started with a local LLM environment using **Ollama** for fast and private AI inference.
- **LLAMA 3.2 Model**: Leverage Facebook's LLAMA 3.2 (llama3.2:3b) for state-of-the-art natural language processing capabilities.
- **Chat History Management**: The chatbot can maintain conversational context, allowing for more meaningful and coherent interactions.
- **Streamlit Integration**: A clean, simple interface for user interaction, built using **Streamlit**.

## Prerequisites

Ensure the following are installed on your system:
- **Python 3.8+**
- **Ollama** installed with LLAMA 3.2 model (llama3.2:3b)
- **Streamlit** for the interface
- **Langchain** for chatbot development

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/deepakbhagatiitr/Ollama-bot.git
   cd ollama-chatbot
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Ensure Ollama and LLAMA 3.2 model are correctly set up by following the [Ollama Installation Guide](https://ollama.com/docs/getting-started).

### Running the Chatbot

To start the chatbot, simply run the following command:

```bash
streamlit run .\app.py
```

This will launch the Streamlit app in your browser, where you can interact with the chatbot.
