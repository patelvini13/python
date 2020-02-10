def ChkPrime(n):
    for i in range(2,n):
        if(n%i == 0):
            return 1
        else:
            return 0