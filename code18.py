s = input("Enter a string: ")
sub = input("Enter substring: ")

count = 0

for i in range(len(s)):
    if s[i:i+len(sub)] == sub:
        count = count + 1

print("Occurrences:", count)