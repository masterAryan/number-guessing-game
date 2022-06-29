print("lets play number guessing game ")
chances = int(input("guess a nuber between 1 and 9:"))
while chances >5 :
    
    import random 
    guess = round(random.uniform(1,9))
    print (guess)

    if chances == guess :
        print("you are correct")
       
        break
        
    else :
        print("wrong try again")
        
        break
    
