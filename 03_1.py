# with open ('data/fruits.txt', 'r') as f:
#     fruits = f.readlines()
# print(fruits) # \n 같이 출력됨

# \n 삭제 방법
with open ('data/fruits.txt', 'r') as f:

    fruits = f.read().split('\n') # 1 .read() 를 이용한 것
    print(fruits)

with open ('data/fruits.txt', 'r') as f:
    fruits = f.readlines()        # 2 .readlines() 를 이용한것 
fruits = [line.rstrip('\n') for line in fruits]
print(fruits)

with open ('data/fruits.txt', 'r') as f:
    fruits = f.readlines()      # 2-1 for 문 사용
    for fruit in fruits:
        fruit = fruit.strip()
        print(fruits)