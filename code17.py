s = input("Enter a string: ")

vowels = ['a', 'e', 'i', 'o', 'u',
          'A', 'E', 'I', 'O', 'U']

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
              'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
              'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
              'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '-', '_', '+', '=', '.', ',', '?', '/']

vowel_count = 0
consonant_count = 0
digit_count = 0
special_count = 0

for ch in s:

    if ch in vowels:
        vowel_count = vowel_count + 1

    elif ch in consonants:
        consonant_count = consonant_count + 1

    elif ch in digits:
        digit_count = digit_count + 1

    elif ch in special:
        special_count = special_count + 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Digits:", digit_count)
print("Special characters:", special_count)