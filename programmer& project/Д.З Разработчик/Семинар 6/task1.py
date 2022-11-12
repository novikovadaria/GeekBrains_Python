from task1_api import sum, divide, multiply, sub
import re
expression = input('Введите выражение: ')
pattern = '\s+'
result = re.split(pattern, expression, maxsplit=2)
if result[1] == '+':
    print(sum(int(result[0]), int(result[2])))
elif result[1] == '-':
    print(sub(int(result[0]), int(result[2])))
elif result[1] == '/':
    print(divide(int(result[0]), int(result[2])))
elif result[1] == '*':
    print(multiply(int(result[0]), int(result[2])))
else:
    print('Неверный оператор')
