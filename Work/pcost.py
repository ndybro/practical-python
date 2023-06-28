# pcost.py
#
# Exercise 1.27
shares = 0
price = 0.0
cost = 0.0
with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f).split(',')
    for line in f:
        row = line.split(',')
        shares = int(row[1])
        price = float(row[2])
        cost = cost + (price*shares)

print(cost)
