x = int(input("Введите натуральное число: "))
answer = ""

while x > 0:
    y = str(x % 2)
    answer = y + answer
    x = int(x / 2)

print(answer)
