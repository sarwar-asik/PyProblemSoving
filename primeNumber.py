# 15. Python program to check whether the given integer is a prime number or not

num = int(input("Enter an integer greater than 1  ::: "))

isPrime = True

for i in range(2, num//2):
    print(i, "range ", num//2)
    if num % i == 0:
        isPrime = False
        break

if isPrime:
    print(num, "is prime number")
else:
    print(num, "is not a prime number")

