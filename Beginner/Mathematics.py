import math


friends = 5
#friends = friends + 1
friends += 1
#friends = friends - 1
friends -= 1
#friends = friends * 3
friends *= 3
#friends = friends / 2
friends /= 2
#friends = friends ** 2
friends **= 2
remainder = friends % 3

x = 3.14
y = 4
z = 5

#result = round(x)
#result = abs(y)
#result = pow(4, 3)
#result = max(x , y, z)
#result = min(x , y, z)

#print(math.pi)
#print(math.e)
#result = math.sqrt(x)
#result = math.ceil(x) #always round up the float
#result = math.floor(x) #opposite the ceil

radius = float(input('Enter the radius of a circle: '))
circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)
print(f"The circumference is: {round(circumference, 2)}cm")
print(f"The area of the circle is: {round(area, 2)}cm")




