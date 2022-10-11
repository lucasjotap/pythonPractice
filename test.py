body_parts = ['head', 'rlight', 'lleg', 'rarm', 'larm', 'body']

"""""
for i in reversed(body_parts):
    body_parts.remove(i)
    print(body_parts)
num = len(body_parts)
print(num)

for i in body_parts[:]:
    body_parts.remove(i)
    print(body_parts)



print(body_parts[0])

"""""


x = int(input("Type you first grade here and I'll tell you whether you've passed: "))
y = int(input("Type you second grade here and I'll tell you whether you've passed: "))
z = int(input("Type you third grade here and I'll tell you whether you've passed: "))

if (x >= 7) and (y >= 7) and (z >= 7):
    print("There ya go! You've passed.")
else:
    print("Seems like one of your grades needed a few more points.")