item = []

for item_number in range(5):
    new_item = {'item':'pen','color':'blue','type':'ball'}
    item.append(new_item)
print(item[0])

for x in item[:1]: 
    if x['color'] == 'blue':
        x['color'] = 'red'

print(x)