# Question:- A spam comment is defined as a text consisting following keywords:
# "Make a lot of money","buy now","subscribe this","click this". Write a program to detect these spams.

c1 = "Make a lot of money"
c2 = "buy now"
c3 = "subscribe this"
c4 = "click this"

message = input("Type any message you want = ")

if((c1 in message) or (c2 in message) or (c3 in message) or (c4 in message)): # in keyword is used to search the particular word or sentence in the any paragraph or line or sentence
    print("You can't type this message as this is a spam message")
else:
    print("Message sent!!")