n=int(input("enter the size of array"))

arr=[]

for i in range(n):
    a=int(input("enter elements into the array"))
    arr.append(a)

print("original array",arr)


print("reversed array",arr[i::-1])

