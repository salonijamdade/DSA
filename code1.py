n=int(input("enter size of array"))
arr=[]

for i in range (n):
    a=int(input("enter numbers in to the array"))
    arr.append(a)


sum=0

for i in arr:
    sum+=i

print(sum)