def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


number = int(input("Введите число: "))

list_nums = []
for i in range(1, number + 1):
    list_nums.append(mult(i))

print(list_nums)
