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
    f.write('''Boysenberry 3
Blueberry 4
Avocado 1
Marionberry 3
Date 9
Cherimoya 7
Redcurrant 9
Longan 4
Mangosteen 4
Cloudberry 5
Loquat 11
Plumcot 8
Soursop 1
Grapefruit 1
Apricot 3
Juniper berry 5
Feijoa 8
Blackcurrant 4
Cantaloupe 6
Salal berry 4
Fig 4
Papaya 5
Elderberry 1
Yuzu 10
Quince 2
Jackfruit 12
Orange 1
Ugli fruit 4
Nance 1
Olive 7
Cherry 7
Pomelo 7
Mulberry 2
Blood orange 1
Plum 2
Lemon 10
Coconut 2
Raspberry 4
Persimmon 1
Bilberry 4
Dragonfruit 3
Cranberry 4
Durian 2
Honeyberry 4
Pineapple 2
Watermelon 1
Rambutan 2
Plantain 6
Pear 5
Goji berry 2
Mango 6
Tamarind 4
Apple 3
Solanum quitoense 8
Star fruit 1
Banana 2
Cucumber 15
Tamarillo 6
Strawberry 3
Raisin 3
Guava 4
Jambul 4
Satsuma 3
Gooseberry 3
Kumquat 7
Nectarine 1
Salak 12
Prune 3
Clementine 2
Lime 4
Currant 2
Purple mangosteen 2
Kiwifruit 1
Damson 2
Physalis 2
Huckleberry 2
Chico fruit 2
Salmonberry 3
Jujube 1
Custard apple 4
Passionfruit 2
Grape 2
Pomegranate 4
Lychee 4
Mandarine 7
Kiwano 5
Honeydew 9
Tangerine 4
Peach 1
Jabuticaba 8
Blackberry 4
Miracle fruit 9
Melon 1
berryfake 1''')