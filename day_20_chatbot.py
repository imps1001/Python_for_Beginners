def main():
    print("Welcome to ChatBot ! Type bye to exit.")
    
    while True:
        user_input = input('You : ')
        if user_input.lower() == 'bye':
            print("ChatBot:", chatbot_response(user_input))
            break
        print("ChatBot:", chatbot_response(user_input))

def chatbot_response(user_input):
    responses ={
         "hi": "Hello! How can I assist you today?",
        "how are you": "I'm doing well, thank you for asking!",
        "bye": "Goodbye! Have a great day!",
        "name": "My name is Jarvis. What's yours?",
        "place an order": "Ok, you can place it on www.codeatrandom.com",
        "age": "I am just a computer program, so I don't have an age.",
        "tech stack": "I use Python, Java, C++, HTML, CSS, JavaScript, and React.",
        "favorite color": "My favorite color is blue.",
        "favorite book": "My favorite book is Harry Potter .",
        "favorite website": "My favorite website is www.codeatrandom.com .",
        "what else ?":"That's all for now.",
		"what courses do you offer?": "We offer a wide range of courses including Web Development, Python, Java",
        "how to enroll?":" You can enroll in a course by visiting our website and following the enrollment process.",
    }
    user_input= user_input.lower()

    for keyword,response  in responses.items():
        if keyword in user_input:
            return response
    
    return "Sorry I don't understand"


if __name__=='__main__':
    main()