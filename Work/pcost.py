# pcost.py
#
# Exercise 1.32
def portfolio_cost(filename):
    import csv
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
cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
