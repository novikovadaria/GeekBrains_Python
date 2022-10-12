number = int(input("Введите число: "))
sum = 0
while (number != 0):
    sum = sum + number % 10
    number = number // 10
print("Сумма цифр числа равна: ", sum)
