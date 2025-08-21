num = int(input("Enter a positive number: "))  

if num % 7 == 0 and num % 10 == 5:
    print("Yes, the number is divisible by 7 and the last digit is 5")
else:
    print("No, the number does not meet both the conditions")
