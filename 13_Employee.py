# Emplyee Program
name = input("Enter Employee Name ")
bs = int(input("Enter Basic Salary Of Employee ")) # basic Salary

if bs == 25000 :
    da = bs * 0.1
    hra = bs * 0.2
    total_sal = bs+da+hra
    print(f"{name} your total salary is {total_sal}")
elif bs == 50000 :
    da = bs * 0.3
    hra = bs * 0.4
    total_sal = bs+da+hra
    print(f"{name} your total salary is {total_sal}")
else :
    print("Employee Not Found")