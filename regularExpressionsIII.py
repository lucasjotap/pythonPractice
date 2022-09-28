import re

# email log
email = "From stephen.marquartd@uct.ac.za Sat Jan 5 09:14:16 2009"

# string extraction
y = re.findall('\S+@\S+', email)
print(y)

y = re.findall('^From (\S+@\S+)', email)
print(y)