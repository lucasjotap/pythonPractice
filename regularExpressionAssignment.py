import re

line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
x = re.findall('\S+?@\S+', line)
print(x)