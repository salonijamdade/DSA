n=int(input("enter the size of array"))

arr=[]

for i in range(n):
    a=int(input("enter the elements into the array"))
    arr.append(a)

l1=arr[0]
l2=arr[0]
s1=arr[0]
s2=arr[0]

for i in arr:
    if i>l1:
        l2=l1
        l1=i
    elif i>l2 and l1!=i:
        l2=i
    if i<s1:
        s2=s1
        s1=i
    elif i<s2 and s1!=i:
        s2=i
        



 


print(l1)
print(l2)



print(s1)
print(s2)