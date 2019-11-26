#fibonacci in python3
a = int(input("enter a value"))
f=0
s=1
if (a<=0):
    print("given output seris is",f)
else:
    print(f,s,end="")
    for x in range(2,a):
        next = f+s
        print(next,end="")
        f=s
        s=next
