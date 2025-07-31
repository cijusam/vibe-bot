
from flask import Flask, render_template, request, jsonify
from src.chatbot import Chatbot

app = Flask(__name__)
bot = Chatbot()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    prognosis = bot.get_prognosis(user_input)
    
    if prognosis:
        response = (
            f"<b>Based on your symptoms, you might have:</b> {prognosis['name']}<br><br>"
            f"<b>Prognosis:</b> {prognosis['prognosis']}<br><br>"
            f"<b>Suggested Action:</b> {prognosis['service_suggestion']}"
        )
    else:
        response = "I'm sorry, I couldn't find a matching condition based on your symptoms. Please consult a real doctor."
        
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

