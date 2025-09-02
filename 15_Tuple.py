# Tuple

a = (10,20,30)
print(a)
print(type(a))
print(id(a))

a1 = (10 , "piuu","vivek",0.100)
print(a1)

a3 = [(10,20,30),(10 , "piuu","vivek")]
print(a3)
print(type(a3))
print(a3[0])
print(type(a3[0]))

a4 = [[10,20,30],(40,50,60),['a','b','c']]
print(a4)
print(a4[0])
print(a4[1])

a5 = ([10,20,30],[40,50,60])
print(a5)
print(a5[0])
print(a5[1])

mat = [(1,2,3),(4,5,6),(7,8,9)]
print(mat)
for i in mat :
    print(i)