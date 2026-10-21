def countfreq(n:int)->list[int]:
    count=[0]*10
    for i in str(n):
        count[int(i)]+=1
    return count

n = int(input("Enter a number: "))
print(countfreq(n))
