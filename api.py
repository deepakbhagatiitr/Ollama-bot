from flask import Flask, request, jsonify
from langchain_ollama import ChatOllama
from flask_cors import CORS  # To allow requests from different origins (frontend)
import time

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to generate a response
def generate_response(input_text):
    model = ChatOllama(model="llama3.2:3b", base_url="http://localhost:11434/")
    start_time = time.time()
    try:
        response = model.invoke(input_text)
        # elapsed_time = time.time() - start_time
        # if elapsed_time > 10:
        #     return {"error": "The response is taking longer than expected. Please try again later."}
        return {"response": response.content}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

# Define the POST route for the API
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
