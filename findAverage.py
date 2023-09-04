# 7. Python program to check whether the given integer is a multiple of 5

number = int(input("Enter an Integer ::  "))
multipleNumber = int(input("Which number multiple by :: "))
if number % multipleNumber == 0:
    print(number, "is a multiple by", multipleNumber)
else:
    print(number, "is not a multiple by", multipleNumber)

print("---done---")