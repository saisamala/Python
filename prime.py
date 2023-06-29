def primenum():
    num = int(input("Enter the number: "))
    flag = False
    if num>=1:
        for i in range(2,(num//2)+1):
            if (num % i==0):
                flag = True
    
    if flag:
        print("Not a prime")
    else:
        print("Prime number")

primenum()