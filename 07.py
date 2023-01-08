import json

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성 

# 장르번호의 이름

genre = []

for i in genres_list:
    if i['id'] == movie['genre_ids'][0]:
        genre.append(i['name'])
    if i['id'] == movie['genre_ids'][1]:
        genre.append(i['name'])

print(genre)

# 해설지

ids = movie['genre_ids']
genre = []

for id in ids:
    for i in genres_list:
        if id == i['id']:
            genre.append(i['name'])

print(genre)