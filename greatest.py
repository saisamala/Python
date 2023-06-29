num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))


if num1>num2:
    if num1>num3:
        great = num1
    else:
        great = num3
else:
    if num2>num3:
        great = num2
    else:
        great = num3
print(great)