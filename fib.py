fib = [0,1]

while True:
    num = int(input("enter the amount of characters you want in the list: "))
    [fib.append(fib[-1]+fib[-2]) for i in range(num-2)]

    print(fib)

    choice = input("Do you want to continue? ")

    if choice == 'yes':
        fib = [0,1]
        pass
    else:
        break