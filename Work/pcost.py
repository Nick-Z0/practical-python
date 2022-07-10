# pcost.py
#
# Exercise 1.33
import sys
import csv

def portfolio_cost(filename):
    cost_temp = 0
    f = open(filename)
    rows = csv.reader(f)
    headers = next(f)
    for row in rows:
        try:
            cost_temp = cost_temp + int(row[1]) * float(row[2])
        except ValueError:
            print("Couldn't parse", row) 
    f.close()
    return cost_temp

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
