number = int(input("Choose an integer greater than 2: "))

def checkPrime(input_num):
    x = range(2,input_num)
    b = []

    for i in x:
        if input_num % i == 0:
            b.append(i)

    print("b = " + str(b))

    if len(b)==0:
        return True
    else:
        return False
    

prime = checkPrime(number)
if prime:
    print(str(number) + " is a prime number.")
else:
    print(str(number) + " is NOT a prime number.")
