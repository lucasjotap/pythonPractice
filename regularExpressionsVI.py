import re

line = "From stephen.marquartd@uct.ac.za Sat Jan 5 09:14:16 2009"

y = re.findall('@([^ ]*)', line)

print(y)