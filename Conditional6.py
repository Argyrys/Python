#Check for vowel and consonant

char = input("enter your char:")

Uchar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lchar = "abcdefghijklmnopqrstuvwxyz"

if (char not in Uchar) and (char not in Lchar):
    print("Invalid")
elif char in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")