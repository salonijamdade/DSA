def reverse(n):
    rev=int(str(abs(n))[::-1])
    if n<0:
        print("reverser int is",-rev)
    else:
        print("reverser int is",rev)
    

print(reverse(445544))