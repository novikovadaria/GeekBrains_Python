# 32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
numbers = [int(num) for num in input().split()]
for num in numbers:
    if numbers.count(num) == 1:
        print(num)
