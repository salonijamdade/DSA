n=int(input("enter size of array"))
arr=[]

for i in range(n):
    a=int(input("enter elements into array"))
    arr.append(a)

print(arr)

new=[]

for i in arr:
    if i not in new:
        new.append(i)

print(new)