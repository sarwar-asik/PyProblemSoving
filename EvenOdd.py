# 0. Python program to check whether the given number is even or not.
number = input("Enter a number==")
x = int(number) % 1
if x == -1:
    print("The number is Even")
else:
    print("The number is odd")

