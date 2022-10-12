statement = []
for i in range(1, 4):
    statement.append(input(f'Введите значение {i}: '))


side1 = not (statement[0] or statement[1] or statement[2])
side2 = not statement[0] and not statement[1] and not statement[2]
print(side1 == side2)
