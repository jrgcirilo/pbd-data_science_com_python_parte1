users = [
    {"id": 0, "name": "Hero", "age": 18, "genre": "Male"},
    {"id": 1, "name": "Dunn", "age": 19, "genre": "Male"},
    {"id": 2, "name": "Chi", "age": 20, "genre": "Male"},
    {"id": 3, "name": "Thor", "age": 21, "genre": "Male"},
    {"id": 4, "name": "Clive", "age": 22, "genre": "Male"},
    {"id": 5, "name": "Sue", "age": 18, "genre": "Female"},
    {"id": 6, "name": "Kate", "age": 19, "genre": "Female"},
    {"id": 7, "name": "Anna", "age": 20, "genre": "Female"},
    {"id": 8, "name": "Carolina", "age": 21, "genre": "Female"},
    {"id": 9, "name": "Daisy", "age": 22, "genre": "Female"},
]

friendships = [
    (0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6),
    (3, 7), (3, 8), (4, 9), (4, 0), (5, 1), (5, 2),
    (6, 3), (6, 4), (7, 5), (7, 6), (8, 7), (8, 8),
    (9, 9), (9, 0)
]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def number_of_friends_by_genre (user,genre):
    cont = 0
    for friend in user['friends']:
        if(friend['genre']==genre):
            cont=cont+1
    return cont    

for user in users:
	print({user['id']: (number_of_friends_by_genre(user,'Male'), number_of_friends_by_genre(user,'Female')) 
    })

