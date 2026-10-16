def armstrong(n):
    s=str(n)
    total=0
    for i in s:
        total+=int(i)**len(s)

    return total==n

print(armstrong(153))