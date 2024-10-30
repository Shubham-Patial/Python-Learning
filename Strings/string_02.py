# Write a program to fill the given template

# letter = '''Dear <|Name|>,
# You are selected !
# <|Date|>'''

letter = '''Dear <|Name|>,
You are selected !
<|Date|>'''
print(letter.replace("<|Name|>", "Shubham").replace("<|Date|>", "10-10-2024")) # the replace() method is used to substitute the <|Name|> placeholder with "Shubham" and the <|Date|> placeholder with "10-10-2024"

