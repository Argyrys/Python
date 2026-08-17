#Check if a number is 3 digit or not

n = int(input("Enter your number:"))

if n >= 100 and n <= 999:
    print("Number is 3 Digit")
else:
    print("Number is not 3 Digit")