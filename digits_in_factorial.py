def digitsinfactorial(n:int)->int:
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    print(factorial)

    count=0
    while factorial>0:
        count+=1
        factorial=factorial//10

    return count

n = int(input("Enter n: "))
print(digitsinfactorial(n))