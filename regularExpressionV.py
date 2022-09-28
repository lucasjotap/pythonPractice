# Setting string example
email = "From stephen.marquartd@uct.ac.za Sat Jan 5 09:14:16 2009"

# Separating words in string and inserting them into a list
word = email.split()

# Selecting the first value from the new list (which will be a string of characters since we split it)
x = word[1]

# Printing out the output
print(x)

# Slicing through the element to get what comes after the "@" sign.
y = x.split("@")

# Printing out the output
print(y[1])