try:
    number = int(input('Введите число: '))
    number_list = []
    for i in range(-number, number+1):
        number_list.append(i)
    print(number_list)

    index1 = int(input('Введите позицию первого элемента: '))
    index2 = int(input('Введите позицию второго элемента: '))

    mult = number_list[index1] * number_list[index2]
    print(mult)
except:
    print(f'Введите число от {-number} до {number}')
