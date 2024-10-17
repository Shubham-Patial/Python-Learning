# Ques:- The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi - score. You need to write a program to update the Hi - Score whenever game() breaks the Hi-Score
import random

def game():
    print("You are gonna play this game.....")
    score = random.randint(1, 100) # used to get random number
    with open("High_Score.txt") as f:
        high_score = f.read()
        if high_score != "":
            high_score = int(high_score)
        else:
            high_score = 0
    print(f"Your socre is = {score}")
    if score > high_score:
        with open("High_Score.txt", "w") as f:
            f.write(str(score))
    
    return score

game()