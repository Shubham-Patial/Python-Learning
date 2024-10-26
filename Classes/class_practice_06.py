from random import randint # importing random number from random library
class Game:

    def __init__(harry, number):  # defining the init function which is a constructor and it calls itself when function call is made
        harry.number = number
    def like_game(harry):
        if(harry.number < 20): # conditional statements
            print("You don't love to play any outdoor sport cause your liking score was = {harry.number}")
        elif harry.number >= 20 and harry.number < 60:
            print(f"You like to play Cricket more than Badminton as the liking score was = {harry.number}")
        else:
            print(f"You love to play badminton cause your total for the sports is = {harry.number}")

ga = Game(randint(1, 100))
ga.like_game()

#So talking about the question yeah we can name self as any other naming convention but the only purpose we use self is because it is more relevant naming in programming.