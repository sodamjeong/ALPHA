#1
with open ('data/fruits.txt', 'r') as f:
    fruits = f.readlines()
fruits = [line.rstrip('\n') for line in fruits]

dict = {}
n = 0

for i in fruits:
    if i[-5:] == 'berry':
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
            
with open ('03_sub.txt', 'w') as f:
    for i in dict:
        n += 1
    f.write(str(n) + '\n') 
    for i in dict:
        f.write(i +'\n')



#2 해설지

fruit_list = []
fruit_count = 0

with open('./data/fruits.txt', 'r') as f:
    fruits = f.readlines()
    for fruit in fruits:
        fruit = fruit.strip()
        if fruit[-5:] == 'berry':
            if fruit not in fruit_list:
                fruit_list.append(fruit)
                fruit_count += 1

with open('./03.txt', 'w') as f:
    f.write(str(fruit_count) + '\n')

    for fruit in fruit_list:
        f.write(fruit + '\n')

