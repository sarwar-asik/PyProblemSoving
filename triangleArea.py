
a = input("Write the length of a side =  ")

sideA = float(a)
b = input("Write the length of b side =  ")
sideB = float(b)
c = input("Write the length of c ide =  ")
sideC = float(c)

totalRound = (sideA+sideB+sideC)
s = totalRound/2

area = s*(s-sideA)*(s-sideB)*(s-sideC)
print("Area of the Triangle is ", area)

