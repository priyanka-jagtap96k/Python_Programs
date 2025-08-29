# Reverse number
#num = 1221
num = int(input("Enter A Four Digit Number "))

a1 = (num % 10)*1000
num = num // 10
a2 = (num % 10)*100
num = num // 10
a3 = (num % 10)*10
num = num //10
ans=a1+a2+a3+num
print(ans)