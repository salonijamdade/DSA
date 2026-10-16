def reverse(n):
    rev=int(str(abs(n))[::-1])
    if n<0:
        return -rev
    return rev

print(reverse(445544))