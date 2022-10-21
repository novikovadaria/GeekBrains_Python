# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def nums(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    return ans


print(nums(int(input())))
