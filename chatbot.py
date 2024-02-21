def chatbot_response(user_input):
    responses = {
        "hi": "Hello! How can I assist you today?",
        "how are you": "I'm doing well, thank you for asking!",
        "bye": "Goodbye! Have a great day!",
        "name": "My name is Jarvis. What's yours?",
        "place an order": "Ok, you can place it on www.amazon.com",
        "age": "I am just a computer program, so I don't have an age.",
        "tech stack": "I use Python, Java, C++, HTML, CSS, JavaScript, and React.",
        "favorite color": "My favorite color is blue.",
        "favorite food": "My favorite food is Momos.",
        "favorite movie": "My favorite movie is RRR.",
        "favorite song": "My favorite song is Bum Bum Bole.",
        "favorite book": "My favorite book is Harry Potter .",
        "favorite website": "My favorite website is www.google.com .",
        "What else ?":"That's all for now."
    }
    
    # Convert user input to lowercase for case insensitivity
    user_input = user_input.lower()
    
    # Check if user input matches any predefined responses
    for keyword, response in responses.items():
        if keyword in user_input:
            return response
    
    # If no match is found, return a default response
    return "I'm sorry, I didn't understand that."

def main():
    print("Welcome to ChatBot! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("ChatBot:", chatbot_response(user_input))
            break
        
        print("ChatBot:", chatbot_response(user_input))

if __name__ == "__main__":
    main()
