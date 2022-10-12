number = int(input('Введите число: '))
number_list = []
sum = 0
sum_list = []
for i in range(1, number+1):
    number_list.append((1+1/number)**number)
for num in number_list:
    sum += num
    sum_list.append(sum)

print(sum_list)
