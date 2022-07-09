# pcost.py
#
# Exercise 1.27
cost = 0
f = open('Data/portfolio.csv', 'rt')
headers = next(f)
for line in f:
    row = line.split(',')
    cost = cost + int(row[1]) * float(row[2])
f.close()
print(cost)
