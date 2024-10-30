# Question:- Write a program to find out whether a given post is talking about "Harry" or not

post_message = input(" Type your blog post here = ")

if ("Harry" in post_message): # checks if Harry word is present in the post_message variable
    print("The post is talking about Harry")
else:
    print("The post is not talking about Harry")