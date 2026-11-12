def anagram(n1: int, n2: int) -> bool:
    count = [0] * 10
    for i in str(n1):
        count[int(i)]+=1

    for i in str(n2):
        count[int(i)]-=1
    print(count)
    for i in count:
        if i!=0:
            return False
    return True

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print(anagram(n1, n2))
    