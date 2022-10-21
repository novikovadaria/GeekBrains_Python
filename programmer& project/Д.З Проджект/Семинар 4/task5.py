# 30. Есть два файла: в одном хранятся ФИО пользователей сайта,
# а в другом — данные об их хобби. Известно, что при хранении данных используется принцип:
# одна строка — один пользователь. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.


dictionary = {}
users = []
hobbis = []

with open('user.txt', encoding='utf-8') as file1:
    for user in file1:
        users.append(user)


with open('hobby.txt', encoding='utf-8') as file2:
    for hobby in file2:
        hobbis.append(hobby)
print(users)
print(hobbis)
for man in users:
    for hobby in hobbis:
        dictionary[user] = hobby


with open('users_hobby.txt', 'w', encoding='utf-8') as file3:
    file3.write(dictionary)
