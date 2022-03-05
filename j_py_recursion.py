# recursive function is a function that calls itself


def calc_sum(n):
    if n == 1:
        return 1
    else:
        return n + calc_sum(n - 1)


sum = calc_sum(5)
print(sum)
