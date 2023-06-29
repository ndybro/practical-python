# pcost.py
#
# Exercise 1.27
import csv
import sys
def portfolio_cost(filename):
    costlocal = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                shares = int(row[1])
                price = float(row[2])
                costlocal = costlocal + (price*shares)
            except ValueError:
                print("Couldn't parse", row)
        return costlocal


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
