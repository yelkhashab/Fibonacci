loop = 1
while loop == 1:
    check = 1
    count = 0
    iterations = 0
    fib = 0
    prev = 0
    nextfib = 0
    seq = []
    prev = input("Enter first value: ")
    try: prev = int(prev)
    except: 
        print("The entered value was inputted incorrectly")
        check = 0
        rerun()
    fib = input("Enter second value: ")
    try: fib = int(fib)
    except: 
        print("The entered value was inputted incorrectly")
        check = 0
        rerun()
    iterations = input("The program will output the sequence up to the nth term. Enter your prefered value for n:")
    try: iterations  = int(iterations)
    except: 
        print("The entered value was inputted incorrectly")
        check = 0
        rerun()
    seq.append(prev)
    seq.append(fib)
    while count <= iterations:
        count = count + 1
        nextfib = prev + fib
        prev = fib
        fib = nextfib
        seq.append(nextfib)
    if check == 1:
        print (str(seq).strip('[]'))

    def rerun():
        YN = input("Do you want to rerun the program with different values? ")
        if YN[0].upper() == 'Y':
            loop = 0
        elif YN[0].upper() == 'N':
            loop = 1
            exit()
        else:
            print("The inputted value was invalid")
            exit()
        

