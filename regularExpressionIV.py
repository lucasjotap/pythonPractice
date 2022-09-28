# email log
email = "From stephen.marquartd@uct.ac.za Sat Jan 5 09:14:16 2009"
# finding the "@" position without re
position_one = email.find("@")
print(position_one)
# finding the whitespace after "position_one"
position_two = email.find(' ',position_one)
print(position_two)
# extracting data from string "email"
host = email[position_one+1 : position_two]
print(host)