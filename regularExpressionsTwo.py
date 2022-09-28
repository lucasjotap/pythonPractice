# import re lib
import re 

x = "From: Using the : character"

# find any string starting in F 
y = re.findall('^F.+:',x)
print(y)

x = "From: Using the : character"

# find any string starting in F and don't be greedy
y = re.findall('^F.+?:',x)
print(y)
