# import re lib
import re 

# using a regular expression to find numbers in a string
x = "My favorite numbers 2 are 19 and 9"

# find one or more digits in a string
y = re.findall('[0-9]+',x)
print(y)

# find all substrings in x string
y = re.findall('[AEIOU]+', x)
print(y)

