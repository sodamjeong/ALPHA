with open('data/fruits.txt', 'r', encoding='UTF8') as f:
    fruits = f.readlines()

 
n = 0

for i in fruits:
    n += 1

print(n)


f = open('02.txt', 'w')
f.write('394')
f.close()