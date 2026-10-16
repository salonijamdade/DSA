def is_palindrom(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False

print(is_palindrom(123321))