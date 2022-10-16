# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
lenght = int(input('введите размер массива: '))
numbers = []
for e in range(1, lenght+1):
    numbers.append(int(input(f'введите {e} элемент массива: ')))


mult_nums = []
while len(numbers) != 0:
    mult = numbers[0] * numbers[-1]
    mult_nums.append(mult)
    numbers.remove(numbers[0])
    numbers.remove(numbers[-1])
# print(numbers)
print(mult_nums)
