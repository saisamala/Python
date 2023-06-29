def armstrong(num):
    duplicate = num
    temp = num
    count = 0

    while temp>0:
        temp = temp // 10
        count +=1

    sum = 0
    while num>0:
        rem = num % 10
        sum += rem ** count
        num = num//10

    if duplicate == sum:
        print("Armstrong number")
    else:
        print("not Armstrong")

def prime(num):
    flag = False
    if num>=1:
        for i in range(2,(num//2)+1):
            if (num % i==0):
                flag = True
    
    if flag:
        print("Not a prime")
    else:
        print("Prime number")

def sumOfNumbers(num):
    
    sum = 0
    while(num>0):
        temp = num%10
        sum +=temp
        num = num //10
    print(f"sum = {sum}")



def options():
    print("Select 1 for Armstrong")
    print("Select 2 for Prime number")
    print("Select 3 for Sum of the number")
    option = input("Enter the option: ")

    if option=="1":
        armstrong(num)
    elif option=="2":
        prime(num)
    elif option=="3":
        sumOfNumbers(num)
    else:
        print("Please enter a valid number")
        options()


num = int(input("Enter your number: "))

options()