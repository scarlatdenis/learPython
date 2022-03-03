num = 407
flag = 1

for i in range(2, num):
    if (num % i) == 0:
        print(num, "is not a prime number")
        print(i, "times", num // i, "is", num)
        flag = 0
        break
    if  flag == 1:
        print(num, "is a prime number")

