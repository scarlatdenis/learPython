while True:
    try:
        a = int(input("Enter a number: "))
        print("Your number is: ", a)
        break
    except:
        print("Invalid input.")
        break
