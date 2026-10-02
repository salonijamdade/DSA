n=int(input("enter the size of array"))

arr=[]

for i in range(n):
    a=int(input("enter elements into the array"))
    arr.append(a)

target=int(input("enter the target element from the array"))

for i in range(len(arr)):
    if arr[i]==target:
        print("target is present in the array list",arr[i])
    else:
        print("target is not present in the array list")   

