#palindrome code in python3
n = int(input("enter values"))
temp = n
rev = 0
while(n>0):
    dig = n%10
    rev = rev*10+dig
    n=n//10
if (temp == rev):
    print("enter  is palindrome")
else:
    print("no is not palindrome")
