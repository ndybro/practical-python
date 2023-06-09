# bounce.py
#
# Exercise 1.5

height = 100

for i in range(10):
    height = height - ((2/5)*height)
    print(round(height, 4))