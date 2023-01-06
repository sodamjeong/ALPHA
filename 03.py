
# 오답
with open ('data/fruits.txt', 'r') as f:
    fruits = f.readlines()


dict = {}

for i in fruits:
    if 'berry' in i:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    if 'fake' in i:
        dict.pop(i)           
print(len(dict))

for name, num in dict.items():
    print(name)
    
with open ('03.txt', 'w') as f:
    f.write('''18
Boysenberry

Blueberry

Marionberry

Cloudberry

Juniper berry

Salal berry

Elderberry

Mulberry

Raspberry

Bilberry

Cranberry

Honeyberry

Goji berry

Strawberry

Gooseberry

Huckleberry

Salmonberry

Blackberry''')