# Question:- What will be the length of following Set S:-
# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")

s = set()
s.add(20)
s.add(20.0)
s.add("20")
l = len(s) # counting the length
print(l) # counting length
print(s) # The output you will see is kind a different as you will be expecting {20, 20.0, '20'} but set treat 20.0 as 20 so no duplicate value so only {20, '20'}