class Solution:
    a = 5

o = Solution()
print(o.a) #prints the class attribute because instance attribute is not present
o.a = 0 # Instance attribute is set
print(o.a) # prints the instance attribute because instance attribute is present
print(Solution.a) #Prints the class attribute so acc to question it does not change the class attribute