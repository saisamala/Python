
def factorial(num):
    fact = 1

    while num>0:

        fact *= num
        num -= 1
    return fact

n = int(input("Enter n value: "))
r = int(input("Enter r value: "))

option = input("\n\n1.Permutation \n2.Combination\n\n\nSelect option: ")

if option == "1":
    result = (factorial(n))/(factorial(n-r))
    print(f"The nPr value is: {result}")
elif option == "2":
    result = (factorial(n))/((factorial(r))*(factorial(n-r)))
    print(f"The nCr value is: {result}")
else:
    print("Enter a valid option")

