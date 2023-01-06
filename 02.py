with open('data/fruits.txt', 'r', encoding='UTF8') as f:
    fruits = f.readlines()

 
with open('02.txt', 'w') as f:
    n = 0
    for i in fruits:
        n += 1
    f.write(str(n))
