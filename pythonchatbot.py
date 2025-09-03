def chatbot():
    print("🤖 Hello! I'm CodeBot. Type 'exit' to end the chat.\n")
    while True:
        user = input("You: ").lower()
        if user == 'hello':
            print("Bot: Hi there!")
        elif user in ['how are you', 'how are you?']:
            print("Bot: I'm good, how about you?")
        elif user == 'bye':
            print("Bot: Goodbye! Take care.")
        elif user == 'exit':
            print("Bot: Chat ended.")
            break
        else:
            print("Bot: I didn't understand that.")

chatbot()