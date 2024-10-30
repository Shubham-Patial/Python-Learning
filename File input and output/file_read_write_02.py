# Ques:- The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi - score. You need to write a program to update the Hi - Score whenever game() breaks the Hi-Score
import random # python library to import random numbers 

def game(): # initializing the function
    print("You are gonna play this game.....")
    score = random.randint(1, 100) # random.randint is used to get random number from and range in this case from 1 to 100
    with open("High_Score.txt") as f: # opened the file
        high_score = f.read() # reading the file
        if high_score != "": # conditional statement  
            high_score = int(high_score)
        else:
            high_score = 0
    print(f"Your socre is = {score}")
    if score > high_score: # Another conditional statement
        with open("High_Score.txt", "w") as f: # opening the file in write mode
            f.write(str(score)) # write the score in it
    
    return score

game()