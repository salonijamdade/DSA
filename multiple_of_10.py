def roundnearest(s:str)-> str:
    n=int(s)
    last=n%10
    if n<=5:
        return n-last
    else:
        return n+(10-last)

    return ""

s = input("Enter a number: ")
print(roundnearest(s))