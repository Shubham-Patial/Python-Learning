import random # library to get random number
number = random.randint(1, 100)  # generating the random number from 1 to 100 and storing it in number variable
a = -1
guesses = 1
while(a != number): # using while loop to run until the user guesses the right number
    a = int(input("Guess the number: ")) 
    if(a >number):
        print("Lower number please")
        guesses +=1
    elif(a<number):
        print("Higher number Please") # if elif ladder 
        guesses +=1

print(f"You have guessed the number {number} correctly in {guesses} attempts") # printing the message