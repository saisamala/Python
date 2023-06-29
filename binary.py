num = 10

rev =""
while (num>0):
    temp = num % 2
    rev += str(temp)
    num = num // 2

print(rev)