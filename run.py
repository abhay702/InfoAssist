from flask import Flask, request, jsonify, render_template
import os
import pickle
from sentence_transformers import SentenceTransformer
from data_manager import load_data
from model_manager import get_response, update_embeddings
from config import config 

# Configuration loaded from environment variables with fallback defaults
MODEL_NAME = os.getenv('MODEL_NAME', "models/all-MiniLM-L6-v2")
DATA_FILE = os.getenv('DATA_FILE', "data/dialogs.txt")
EMBEDDINGS_FILE = os.getenv('EMBEDDINGS_FILE', "pickle/embeddings.pkl")
FAQ_DATA_FILE = os.getenv('FAQ_DATA_FILE', "pickle/faq_data.pkl")

app = Flask(__name__)
sentence_model = SentenceTransformer(MODEL_NAME)

@app.route("/")
def welcome():
    return render_template("chatbot.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/get_answer", methods=["POST"])
def get_answer():
    data = request.get_json()
    question = data.get("question").strip()
    if question.lower() == "quit":
        return jsonify({"answer": "Goodbye! Have a nice day!", "quit": True})
    else:
        answer, similarity, similar_questions = get_response(question)
        return jsonify({
            "answer": answer,
            "similarity": similarity.tolist(),
            "similar_questions": similar_questions,
            "quit": False
        })

@app.route("/get_similar_questions", methods=["POST"])
def get_similar_questions():
    data = request.get_json()
    similarity = data.get("similarity")
    df = load_data(DATA_FILE)
    top_indices = sorted(range(len(similarity)), key=lambda i: similarity[i], reverse=True)[1:6]
    similar_questions = [df.iloc[i]["question"] for i in top_indices]
    return jsonify({"similar_questions": similar_questions})

@app.route("/get_selected_answer", methods=["POST"])
def get_selected_answer():
    data = request.get_json()
    selected_question = data.get("selected_question")
    answer, _, _ = get_response(selected_question)
    return jsonify({"answer": answer})

@app.route("/add_question", methods=["POST"])
def add_question():
    data = request.get_json()
    new_question = data.get("question").strip()
    new_answer = data.get("answer").replace("\n", "\\n").strip()  # Replace newline characters with \n and strip any leading/trailing whitespace

    # Append new question and answer to dialogs.txt
    with open("data/dialogs.txt", "a") as file:
        file.write(f"\nQ: {new_question}\nA: {new_answer}\n")

    # Update the DataFrame and embeddings without restarting the server
    update_data()

    return jsonify({"message": "Question added successfully"})

    
def update_data():
    global df, question_embeddings, faq_data
    df = load_data(DATA_FILE)
    question_embeddings = sentence_model.encode(df["question"].tolist(), convert_to_tensor=True)
    faq_data = df
    with open(EMBEDDINGS_FILE, "wb") as emb_file:
        pickle.dump(question_embeddings, emb_file)
    with open(FAQ_DATA_FILE, "wb") as data_file:
        pickle.dump(df, data_file)

# Load data initially when the module is loaded
df, question_embeddings, faq_data = None, None, None
update_data()
