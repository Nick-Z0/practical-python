# pcost.py
#
# Exercise 1.30
def portfolio_cost(filename):
    cost_temp = 0
    f = open(filename, 'rt')
    headers = next(f)
    for line in f:
        row = line.split(',')
        cost_temp = cost_temp + int(row[1]) * float(row[2])
    f.close()
    return cost_temp
cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
