
num1 = int(input("Enter numerator value: "))
num2 = int(input("Enter denominator value: "))


try:
    result = num1/num2
except ZeroDivisionError:
    result = "Indeterminate value"

print(result)
    