with open ('01.txt','w',encoding='UTF8') as f:
    f.write('Hello, Python!')
    for n in range(1,6):
        f.write(f'\n{n}일차 파이썬 공부 중')



# with open('01.txt', 'w', encoding='UTF8') as f:
#     f.write('''Hello, Python!
# 1 일차 파이썬 공부 중
# 2 일차 파이썬 공부 중
# 3 일차 파이썬 공부 중
# 4 일차 파이썬 공부 중
# 5 일차 파이썬 공부 중''')