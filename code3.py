n=int(input("enter the size of array"))

arr=[]

for i in range(n):
    a=int(input("enter elements into array"))
    arr.append(a)

odd=0
even=0

for i in arr:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1


print("count of even number",even)
print("count of odd number",odd)