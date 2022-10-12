sentence = input('Введите первую строку: ')
sentence_list = sentence.split()
what_to_find = input('Введите вторую строку: ')
what_to_find_list = what_to_find.split()
count = 0
for word in sentence_list:
    if word in what_to_find_list:
        count += 1
print(count)
