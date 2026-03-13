import re
import random
from datetime import datetime

class RuleBasedChatbot:
    def __init__(self):
        # Dictionary of rules: Regex patterns mapped to possible responses
        self.rules = {
            r'\b(hi|hello|hey|greetings)\b': [
                "Hello there! How can I help you today?",
                "Hi! What's on your mind?",
                "Greetings! How can I assist you?"
            ],
            r'\b(how are you|how are things)\b': [
                "I'm just a rule-based bot, but I'm doing great! You?",
                "Operating at 100% efficiency. How are you doing?"
            ],
            r'\b(what is your name|who are you)\b': [
                "I am PusuBot, a rule-based chatbot created by Pushkar Biring. I am designed to assist with basic queries."
            ],
            r'\b(time|what time is it)\b': [
                self.get_current_time
            ],
            r'\b(help|support|what can you do)\b': [
                "I can say hello, tell you the time, answer basic questions, and chat! Try asking me my name."
            ],
            r'\b(bye|goodbye|quit|exit)\b': [
                "Goodbye! Have a great day.",
                "See you later! Shutting down..."
            ]
        }
        
        # Fallback responses if no patterns match
        self.fallbacks = [
            "I'm sorry, I didn't quite catch that.",
            "Could you rephrase that? My NLP logic is pretty basic.",
            "I don't have a rule for that yet. Can we talk about something else?"
        ]

    def get_current_time(self):
        """Helper function to dynamically generate the current time."""
        now = datetime.now()
        return f"The current time is {now.strftime('%H:%M')}."

    def preprocess_text(self, text):
        """Basic NLP pipeline: lowercase and strip extra spaces."""
        text = text.lower()
        text = text.strip()
        return text

    def get_response(self, user_input):
        """Matches user input against defined regex rules."""
        cleaned_input = self.preprocess_text(user_input)

        # Iterate through the rules dictionary
        for pattern, responses in self.rules.items():
            if re.search(pattern, cleaned_input):
                # Choose a random response from the matched category
                response = random.choice(responses)
                
                # If the response is a function (like time), call it
                if callable(response):
                    return response()
                return response
                
        # If no match is found, return a fallback
        return random.choice(self.fallbacks)

    def chat(self):
        """Main loop to run the chatbot."""
        print("==============================================")
        print("   PusuBot: Rule-Based Chatbot Initialized")
        print("   (Type 'exit' or 'quit' to stop chatting)")
        print("==============================================\n")
        
        while True:
            user_input = input("You: ")
            
            if not user_input.strip():
                continue
                
            response = self.get_response(user_input)
            print(f"PusuBot: {response}")
            
            # Check for exit commands to break the loop
            if re.search(r'\b(bye|goodbye|quit|exit)\b', user_input.lower()):
                break

if __name__ == "__main__":
    # Instantiate and run the chatbot
    bot = RuleBasedChatbot()
    bot.chat()