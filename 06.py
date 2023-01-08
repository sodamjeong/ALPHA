import json

# 아래 코드 수정 금지
movies_json = open("data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성


new_list = []
info = {}
n = 0

for i in movies_list:
    info = {
    'id' : movies_list[n]['id'],
    'title' : movies_list[n]['title'],
    'vote_average' : movies_list[n]['vote_average'],
    'overview' : movies_list[n]['overview'],
    'genre_ids' : movies_list[n]['genre_ids']
}
    n += 1
    new_list.append(info)

print(new_list)

# 해설지

new_list = []

for i in movies_list:
    info = {
        'id' : i['id'],
        'title' : i['title'],
        'vote_average' : i['vote_average'],
        'overview' : i['overview'],
        'genre_ids' : i['genre_ids']
    }

    new_list.append(info)

print(new_list)