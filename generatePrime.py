# 16. Python program to generate the prime numbers from 1 to N

num = int(input("Enter the range of number :::   "))
# here if num =10

for n in range(2, num):
    is_prime = True
    for i in range(2, n):
        if (n % i) == 0:
            is_prime = False
            break
    if is_prime:
        print(n)

# for n in range(2, num):
#     # here n = 3,4,5,6,7,8,9
#     for i in range(2, n):
#         # print('this is i', i)
#         if (n % i) == 0:
#             break
#         else:
#             print(n)


