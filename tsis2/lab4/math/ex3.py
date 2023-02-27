from math import tan, pi
a = int(input("Input number of sides: "))
x = float(input("Input the length of a side: "))
y = a * (x ** 2) / (4 * tan(pi / a))
print("The area of the polygon is: ",y)