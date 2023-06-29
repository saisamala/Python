# num = int(input("Enter your number: "))
# sum = 0

# for i in range(1,num+1):
#     sum += i**3

# print(sum)

#---------------------------------

num = int(input("Enter your number: "))
sum = 0
count = 1

while count<=num:

    sum += count**3
    count += 1

print(sum)

