number = 78
low = 1
high = 100

while True:
    print("Agent Guess:", number)
    
    feedback = input("Enter higher, lower or correct:").lower()
    
    if feedback == "higher":
        low = number + 1
        number = (low + high)//2
        
    elif feedback == "lower":
        high = number - 1
        number = (low + high)//2
        
    elif feedback == "correct":
        print("Agent Guessed Correctly!")
        break
    
    else:
        print("Invalid Feedback ")       
    
    
    