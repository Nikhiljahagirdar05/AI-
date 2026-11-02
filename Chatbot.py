
# Simple Rule-Based Chatbot

print("Chatbot: Hello! Welcome.")
print("Chatbot: Type 'bye' to exit.")

while True:

    # Take input from user
    message = input("You: ").lower()

    # Check predefined patterns
    if "hello" in message or "hi" in message:

        print("Chatbot: Hello! How can I help you?")

    elif "how are you" in message:

        print("Chatbot: I am fine. Thank you!")

    elif "your name" in message:

        print("Chatbot: My name is AI Chatbot.")

    elif "college" in message:

        print("Chatbot: College is a place to learn.")

    elif "bye" in message:

        print("Chatbot: Goodbye! Have a nice day.")
        break

    else:

        print("Chatbot: Sorry, I don't understand.")
