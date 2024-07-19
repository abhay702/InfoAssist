import pandas as pd
import config

def load_data(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()


    questions, answers = [], []
    for line in lines:
        if line.startswith("Q:"):
            questions.append(line[3:].strip())
        elif line.startswith("A:"):
            answers.append(
                line[3:].strip().replace("\\n", "\n")
            )  


    return pd.DataFrame({"question": questions, "answer": answers})

def append_data(question, answer, file_path):
    """ Append a new question and answer to the data file. """
    with open(file_path, "a") as file:
        file.write(f"\nQ: {question}\nA: {answer}\n")
    from model_manager import update_embeddings
    update_embeddings()