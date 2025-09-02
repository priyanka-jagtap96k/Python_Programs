# List - Lists are used to store multiple items in a single variable.

l1 = ["piuu","vivek","oma"]
print(l1)

l2 = ["piuu", 10, 20]
print(l2)

l3 = [["piuu","oma","vivek"],[10,20,30],[3.10,10,"abc"]]
#l3[0]
print(l3[2])
print(l3[0][0]) #index of index
print(l3[0][2])

#matrix
l4 = [[10,20,30],[40,50,60],[70,80,90]]
print(l4)
print(l4[0][0])

l5 = [[10,20],[30,40],[50,60],[70,80]]
print(l5)
print(l5[3][1])
print(l5[1][1]+l5[2][0])

# indexing Start form Zero
# Positive indexing (Forword indexing) 0 1 2...
# Negative indexing (Backword indexing) -1 -2 -3
list = [10,20,30,40,50,60,70,80,90]
print(list[0])
print(list[-5])

# Slicing Operator - [:] operator - [start : (stop)end + 1]

a = [10,20,30,40,50]
print(a[0:1])
print(a[0:2])
print(a[0:4]) # Start From Zero index And End With count 4
print(a[:1]) # Default value is Zero

print(a[1:3])
print(a[3:5])

List = ['abc','pqr','xyz']
print(List[0:2])

#[start : stop + 1 : step] 

A1 = [10,20,30,40,50,60,70,80,90]
A1[0:6:1]

# Add Dublicate
A2 = [10,20,30]
A2.append(30)
print(A2)

#Operators
A3 = [10 ,20,30]
A3.insert(1,90)
print(A3)