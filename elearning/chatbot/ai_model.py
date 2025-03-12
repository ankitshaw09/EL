import spacy
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load spaCy NLP model
nlp = spacy.load("en_core_web_md")

# Load knowledge base
with open("chatbot/knowledge_base.json", "r") as file:
    knowledge_base = json.load(file)

questions = [item["question"] for item in knowledge_base]
answers = [item["answer"] for item in knowledge_base]

# Train TF-IDF vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def get_response(user_input):
    """Finds the best answer using cosine similarity."""
    user_vec = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vec, X).flatten()

    best_match_idx = np.argmax(similarities)
    confidence = similarities[best_match_idx]

    if confidence > 0.5:
        return answers[best_match_idx]
    else:
        return "I'm not sure. Let me create a support ticket for you."
