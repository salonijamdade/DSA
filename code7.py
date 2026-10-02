n=int(input("enter the size of array"))
arr=[]

for i in range(n):
    a=int(input("enter elements into array"))
    arr.append(a)

new=[]
zero=0

for i in arr:
    if i==0:
        zero=zero+1
    else:
        new.append(i)

for i in range(zero):
    new.append(i)

print(new)
