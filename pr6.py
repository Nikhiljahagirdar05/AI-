#simple chatbot

while True:
    msg = input("You:").lower()
    
    if "hello" in msg:
        print("Bot: Hello! How are you?")
        
    elif "name" in msg:
        print("Bot: I am a simple chatbot")
        
    elif "how are you" in msg:
        print("Bot: I am Fine!")
        
    elif "bye" in msg:
        print("Bot: Byeee!! Have a great day a head!!!")
        
    else:
        print("Bot: Sorry. I don't understand.")