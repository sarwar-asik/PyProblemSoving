# 9. Python program to find the average of 10 numbers using while loop

count = 0
sum = 0.0

while count < 5:
    number = float(input("Enter a real number ::  "))
    count = count+1
    sum = sum + number
    avg = sum/5
    print("Average is ::: ", avg)