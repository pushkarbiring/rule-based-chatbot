# Rule-Based Chatbot 🤖

A simple, interactive console chatbot built entirely in Python. I developed this project to understand the core mechanics of conversational agents before diving into complex machine learning models.

It uses a dictionary of predefined rules and Regular Expressions (Regex) to parse user inputs and generate appropriate responses.

## Features

* **Interactive Chat:** Developed a simple, continuous loop chatbot for answering user queries in real-time.
* **Basic NLP Logic:** Implemented text preprocessing (lowercasing, whitespace stripping) and Regex pattern matching to identify user intent regardless of phrasing.
* **Dynamic Responses:** The bot can return random responses from a list to feel more natural, and can execute functions dynamically (like fetching the current system time).
* **Fallback Mechanisms:** Gracefully handles unknown inputs with standard fallback responses.

## Technologies Used

* **Language:** Python 3.x
* **Libraries:** `re` (Regular Expressions), `random`, `datetime`

## Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/pushkarbiring/rule-based-chatbot.git
cd rule-based-chatbot

```


2. **Run the script:**
No external dependencies (`pip install`) are required as this uses pure Python standard libraries!
```bash
python chatbot.py

```



## Project Output Preview

When you run the script, it launches an interactive chat session directly in your terminal:

```text
==============================================
   PusuBot: Rule-Based Chatbot Initialized
   (Type 'exit' or 'quit' to stop chatting)
==============================================

You: Hello there!
PusuBot: Greetings! How can I assist you?
You: what is your name?
PusuBot: You can call me PyBot. I'm here to answer basic queries.
You: what time is it?
PusuBot: The current time is 14:30.
You: make me a coffee
PusuBot: Could you rephrase that? My NLP logic is pretty basic.
You: bye
PusuBot: See you later! Shutting down...

```

## Support 💖

If you found this project helpful or just want to support a fellow developer's coding journey, I'd really appreciate it!

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/mrpusu)

[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/PushkarBiring)

Your support helps me continue building open-source projects and learning AI/ML. 🚀

⭐ If you like this project, consider giving it a star!