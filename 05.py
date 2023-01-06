import json

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성

# from pprint import pprint
# pprint(movie)


key = ['id', 'title', 'vote_average', 'overview', 'genre_ids']
info = {}

for k in key:
   info[k] = movie[k]

print(info)
