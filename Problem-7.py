def division(num):
    for i in range(2, num):
        if num % i == 0:
            return -1
    return 0




i = 1
ls = [2]
num = 3
while i < 10001:
    if division(num) == 0:
        ls.append(num)
        i += 1
    num += 1

print(ls[10000])


