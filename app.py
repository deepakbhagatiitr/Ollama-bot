from flask import Flask, request, jsonify
from langchain_ollama import ChatOllama
from flask_cors import CORS
import time
import re

app = Flask(__name__)
CORS(app)

def generate_response(input_text):
    model = ChatOllama(model="llama3.2:3b", base_url="http://localhost:11434/")
    try:
        # Generate response using the model with summarization enabled
        response = model.invoke(input_text, options={"summarization": True})
        bot_response = response.content
        
        # Clean up unwanted markdown styling
        bot_response = re.sub(r'\*\*([^*]+)\*\*', r'\1', bot_response)

        return {"response": bot_response}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

@app.route('/chat', methods=['POST'])
def chat():
    if request.method == 'POST':
        data = request.json
        prompt = data.get('prompt')
        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400
        
        response = generate_response(prompt)
        return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
