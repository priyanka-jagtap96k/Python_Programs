# Armstrong number
#num = 153

"""num = int(input("Enter A Three Digit Number "))

a1 = (num % 10)
num = num // 10
a2 = (num % 10)
num = num //10
ans=a1**3+a2**3+num**3
print(ans)"""

num = int(input("Enter A Three Digit Number "))
temp = num

a1 = (num % 10)**3
num = num // 10
a2 = (num % 10)**3
num = (num //10)**3
ans=a1+a2+num
print(ans)
if temp == ans:
    print("{temp} is Armstrong Number")
else:
    print("{temp} is not Armstrong Number")