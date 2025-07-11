# --- Fix for corrupted or non-standard NLTK installations (Colab/Jupyter) ---
import sys
if 'google.colab' in sys.modules or 'ipykernel' in sys.modules:
    import os
    os.system('pip uninstall -y nltk')
    os.system('pip install --no-cache-dir --upgrade --force-reinstall nltk')

import nltk
import string
import random
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize # Import sent_tokenize

# Ensure NLTK data is available
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')
try:
    # Download the missing 'punkt_tab' resource
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')


lemmatizer = WordNetLemmatizer()

# Simple knowledge base
KNOWLEDGE_BASE = {
    "hello": ["Hi!", "Hello!", "Hey there!"],
    "how are you": ["I'm a bot, but I'm doing well!", "I'm here to help you!"],
    "what is your name": ["I'm your AI chatbot.", "You can call me Chatbot."],
    "what can you do": ["I can answer your questions and chat with you.", "Try asking me about products, services, or general info!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "default": ["I'm not sure I understand. Can you rephrase?", "Sorry, I don't know about that. Try asking something else!"]
}

def preprocess(text):
    text = text.lower()
    text = ''.join([c for c in text if c not in string.punctuation])
    # Use sent_tokenize first, then word_tokenize
    sentences = sent_tokenize(text)
    tokens = [token for sentence in sentences for token in word_tokenize(sentence)]
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmas


def get_response(user_input):
    lemmas = preprocess(user_input)
    for key in KNOWLEDGE_BASE:
        if key == "default":
            continue
        key_lemmas = preprocess(key)
        if all(k in lemmas for k in key_lemmas):
            return random.choice(KNOWLEDGE_BASE[key])
    return random.choice(KNOWLEDGE_BASE["default"])

if __name__ == "__main__":
    print("AI Chatbot (NLP Demo)")
    print("Type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            print("Chatbot: Please enter a message.")
            continue
        response = get_response(user_input)
        print("Chatbot:", response)
        if "bye" in user_input.lower():
            break