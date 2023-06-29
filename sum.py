# n,x = input().split()
# n = int(n)
# x = int(x)

# result = (n-1)*x
# print(result)

#-----------------------------------------

num = int(input("Enter your num: "))
summ=0

while num>0:
    temp = num % 10
    summ += temp
    num = num // 10
print(summ)

#-------------------------------------




