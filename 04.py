with open ('data/fruits.txt', 'r') as f:
    fr = f.readlines()

fr = [line.rstrip('\n') for line in fr]
# data = fr.read().split('\n')

dic = {}

for i in fr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1


for name, num in dic.items():
    print(name,num)


with open ('04.txt', 'w') as f:
    for name, num in dic.items():
        f.write(name + ' ' + str(num) + '\n')