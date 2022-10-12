from unicodedata import numeric


number = input('Введите число: ')
if number.isnumeric() == True:
    number_list = list(number)
    length = len(number_list)
    sum = 0
    if ',' in number_list:
        number_list.remove(',')
        for num in range(length-1):
            int_num = int(number_list[num])
            sum += int_num
    else:
        sum = 0
        for num in range(length):
            int_num = int(number_list[num])
            sum += int_num
    print(sum)
else:
    print('Введите число.')
