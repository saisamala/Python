num = int(input("enter a num: "))

duplicate = num
rev = 0

while num>0:
    temp = num % 10
    rev = rev*10 + temp
    num = num // 10

if (rev==duplicate):
    print(f"{rev} is a pallindrome")
else:
    print(f"{duplicate} is not a pallindrome")