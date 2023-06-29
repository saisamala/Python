# num = (input("Enter your number: "))
# power = len(num)
# sum = 0

# for i in num:
#     sum += int(i)**power

# print(sum)

#---------------------------

num = int(input("Enter your number: "))
duplicate = num
temp= num

count = 0
sum = 0
while temp>0:
    temp = temp // 10
    count += 1

while num>0:
    rem = num % 10
    sum += rem ** count
    num = num // 10

print(sum)

if duplicate==sum:
    print("Armstrong")
else:
    print("not Armstrong")

