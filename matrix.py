#displayingh the values in matrix format
r =int(input("enter how many rows "))
c = int(input("enter how many columns"))
matrix = []
print("enter the values ")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
        matrix.append(a)
for i in range(r):
    for j in range(c):
        print(matrix[i],[j],end="")
    print()
