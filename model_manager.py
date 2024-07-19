from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
from config import config 
from data_manager import load_data  

# Initialize the model
model = SentenceTransformer(config.MODEL_NAME)

def encode_questions():
    """ Encode all questions using the model and save embeddings. """
    df = load_data(config.DATA_FILE)
    embeddings = model.encode(df['question'].tolist(), convert_to_tensor=True)
    with open(config.EMBEDDINGS_FILE, "wb") as emb_file:
        pickle.dump(embeddings, emb_file)

def update_embeddings():
    """ Update embeddings whenever new data is added. """
    encode_questions()

def get_response(query, top_n=5):
    """ Get a response based on the similarity of a query to stored questions. """
    # Load embeddings
    with open(config.EMBEDDINGS_FILE, "rb") as emb_file:
        question_embeddings = pickle.load(emb_file)

    # Load data
    df = load_data(config.DATA_FILE)

    # Compute similarity
    query_embedding = model.encode([query], convert_to_tensor=True)
    similarity = cosine_similarity(query_embedding, question_embeddings)

    # Find top N similar questions
    top_indices = similarity.argsort()[0][-top_n:][::-1]
    best_index = top_indices[0]
    similar_questions = df.iloc[top_indices]['question'].tolist()

    return df.iloc[best_index]['answer'], similarity.flatten(), similar_questions
