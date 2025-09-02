""" Dictionary - { Key : value}
 represent a table details"""

dict = {'ename':'Piuu','sal':90000,'designation':'manager'}
print(dict)

student = {'RollNo':1,
           'Name':"priyanka",
           'clgName':"SVS",
           'Address':'Baramati'}
print(student)

emp = {'ename':['priyanka','vivek','omkar'],
       'sal':[90000,100000,30000],
       'depto':[10,20,30]
       }
print(emp)

print(emp['ename'])
print(emp['ename'][0])

list =[{'a':10,'b':20,'c':30}]
print(list)

my_new_list = [(10,20,30),{10,20,30},[10,20,30],{'a':10,'b':20,'c':30}]
print(my_new_list)