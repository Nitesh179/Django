import random

# Example data feed
data_feed = [
    {
        "input": "What is your name?",
        "response": "My name is Chatbot. Nice to meet you!"
    },
    {
        "input": "How are you?",
        "response": "I'm a chatbot, so I don't have feelings, but thanks for asking!"
    },
    {
        "input": "Tell me a joke",
        "response": "Sure, here's a joke: Why don't scientists trust atoms? Because they make up everything!"
    },
    {
        "input": "Goodbye",
        "response": "Goodbye! Have a great day!"
    }
]

def get_response(user_input):
    for data in data_feed:
        if data["input"].lower() in user_input.lower():
            return data["response"]
    
    # If no matching input found, return a default response
    return "I'm sorry, I don't understand. Can you please rephrase your question?"

def chat():
    print("Welcome to the chatbot! How can I assist you today?")
    
    while True:
        user_input = input("> ")
        response = get_response(user_input)
        print(response)
        
        if user_input.lower() == "goodbye":
            break

# Run the chatbot
chat()