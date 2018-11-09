import math


def individiual(n):
    length_number = math.log(n, 10) + 1
    # print(l)
    return int(length_number)


def number(n):
    while (n != 0):
        n = n / power(10, individiual(n))
        r = n % power(10, individiual(n))
    return int(r)


def power(base, number):
    s = 1
    for i in range(0, number):
        s = s * base
    return s


num = 5432
# individiual(num)
# number(num)
# print(individiual(num))
# print(number(num))
power(individiual(num), number(num))
print(power(individiual(num), number(num)))
