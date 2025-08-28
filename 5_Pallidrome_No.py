"""" Pallidrome Number - when we revere any value it return same value 
        121 - reverse - 121
        madam - reverse - madam"""
num = 121

a1 = num % 10
num = num // 10
a2 = num % 10
num = num //10
ans=a1*100+a2*10+num
print(ans)
