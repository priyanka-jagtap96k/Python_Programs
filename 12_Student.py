student = input("Enter Name of Student ")

s1 = int(input("Enter Eng Marks "))
s2 = int(input("Enter Maths Marks "))
s3 = int(input("Enter Science Marks "))

per = (s1 + s2 + s3)/3.0

print(f"percentage of {student} is {per} ")

if per >= 90 :
    print("Grade A")
elif per >= 80 :
    print("Grade B")
elif per >=70 :
    print("Grade C")
else :
    print("Fail")