# to use regular expression you first import the re lib
import re 

# using a regular expression to find numbers in a string
x = "My favorite numbers 2 are 19 and 9"
y = re.findall('[0-9]+',x)
print(y)

