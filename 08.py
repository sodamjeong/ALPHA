import json

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성




genre = []

for i in genres_list:
    if i['id'] in movie['genre_ids']:
        genre.append(i['name'])

movie['genre_names'] = genre

info = {
    'id' : movie['id'],
    'title' : movie['title'],
    'vote_average' : movie['vote_average'],
    'overview' : movie['overview'],
    'genre_names' : movie['genre_names']
}

print(info)

# 해설지

genre = []
ids = movie['genre_ids']

for id in ids:
    for i in genres_list:
        if id == i['id']:
            genre.append(i['name'])

info = {
    'id' : movie['id'],
    'title' : movie['title'],
    'vote_average' : movie['vote_average'],
    'overview' : movie['overview'],
    'genre_names' : movie['genre_names']
}

print(info)