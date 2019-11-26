#reverse a string using loopsin python3
def reverse(k):
    str = " "
    for i in k:
        str = i + str
    return str
k = input("enter a string" )

print("reverse string is:",end=" ")
print(reverse (k))
