num = int(input("Enter a number: "))

if num % 3 == 0 and num % 10 == 4:
    print("Yes, the number is divisible by 3 and the last digit is 4")
else:
    print("No, the number does not meet both conditions ")