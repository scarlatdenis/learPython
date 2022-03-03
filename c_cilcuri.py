sum = 0

while True:
    n = input("Please enter a number: ")
    n = float(n)

    if n < 0:
        break
    sum += n

print ("Sum: ", sum)

