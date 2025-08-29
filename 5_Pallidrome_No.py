"""" Pallidrome Number - It reads the same from left to right and right to left. 
        121 - reverse - 121
        madam - reverse - madam"""

#num = 121
num = int(input("Enter A Three Digit Number "))

a1 = (num % 10)*100
num = num // 10
a2 = (num % 10)*10
num = num //10
ans=a1+a2+num
print(ans)

#num = 1221
num = int(input("Enter A Four Digit Number "))
temp = num

a1 = (num % 10)*1000
num = num // 10
a2 = (num % 10)*100
num = num // 10
a3 = (num % 10)*10
num = num //10
ans=a1+a2+a3+num
if(temp == ans):
    print("Number is Palindrome Number")
else :
    print("Number is not Palindrome Number")
       


