# Task-3: AI Chatbot with NLP

## 📋 Task Description
Build a chatbot using natural language processing (NLP) libraries like NLTK or spaCy, capable of answering user queries.

**Deliverables:**
- A Python script for the chatbot
- A working chatbot (command-line interface)

---

## 🚀 Solution Overview
This solution implements a simple AI chatbot using the NLTK library for natural language processing. The chatbot can:
- Recognize greetings and farewells
- Answer basic questions about products, services, and general information
- Handle unknown queries gracefully
- Be easily extended with more knowledge

- **Script:** `chatbot.py`

---

## 🗂️ Files in this Folder
| File Name   | Purpose                                      |
|-------------|----------------------------------------------|
| chatbot.py  | Main script for the AI chatbot (NLP-based)   |

---

## ⚙️ How to Run
1. **Install dependencies:**
   ```bash
   py -m pip install nltk
   ```
2. **Run the script:**
   ```bash
   py chatbot.py
   ```
   - The script will automatically download required NLTK data if not already present.
   - Type your message and press Enter to chat with the bot.
   - Type `bye` to exit the chatbot.

---

## 🤖 What the Chatbot Can Do
- Greets the user and responds to greetings
- Answers questions about products, services, support, and more
- Handles farewells and exits gracefully
- Provides default responses for unknown queries
- Uses NLP (tokenization, lemmatization) for better understanding

---

## 📝 Notes
- The chatbot runs in the terminal/command prompt.
- You can expand the knowledge base in `chatbot.py` to add more questions and answers.
- No additional files or data are required.

---

## 🎯 Internship Requirements Met
- ✅ Built with NLTK (NLP library)
- ✅ Answers user queries
- ✅ Python script and working chatbot included 