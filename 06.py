import json

# 아래 코드 수정 금지
movies_json = open("data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성


key = ['id', 'title', 'vote_average', 'overview', 'genre_ids']
info = {}
n = 0

for i in key:
   key[i],movies_list[n][i]
   if i == 'genre_ids':
    n += 1
    