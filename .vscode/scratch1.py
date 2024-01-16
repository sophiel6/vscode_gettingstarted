print("hello, world")

if 5>2:
    print("five greater than 2")

x = 5
x = x*3
print(x)
""" block quote 
"""

print(type(x))
x=str(3)
print(x, type(x))
x, y, z = "sophie", "brennan", "elise"

def sibnames():
    global x 
    x = 'laproscopic'
    print("sophie is " + x)

sibnames()

print("sophie is "+ x)

y = range(6)
print(y)

import random
print(random.randrange(1,10))
print(x[-5:-2])
print("la" in x)

num = 8
x = x + ' {}'
print(x.format(num))

xa = "lala \"Sophie\" lala"
print(xa)
xa += "ha"
print(xa)
