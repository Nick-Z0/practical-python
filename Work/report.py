# report.py
#
# Exercise 2.10
import csv
import sys

def read_portfolio(filename):
    '''
    Reads a stock portfolio file and returns a list of dictionaries of the portfolio file with keys: name, shares, price
    '''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name'   : record['name'],
                'shares' : int(record['shares']),
                'price'  : float(record['price'])
            }
            portfolio.append(stock)

    return(portfolio)

def read_prices(filename):
    '''
    Reads a set of prices file and returns a dictionary with keys: name, price
    '''
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1]) 
            except IndexError:
                pass

    return prices

def make_report(portfolio, prices):
    '''
    Reads a list of stocks and prices and outputs a report list
    '''
    report = []
    portfolio = read_portfolio(filename)
    prices = read_prices(filename2)
    for row in portfolio:
        name = row['name']
        shares = row['shares']
        price = prices[row['name']]
        change = price - row['price']
        report.append((name, shares, price, change))
    return(report)

if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

if len(sys.argv) >= 2:
    filename2 = sys.argv[2]
else:
    filename2 = 'Data/prices.csv'

portfolio = read_portfolio(filename)
prices = read_prices(filename2)
report = make_report(filename, filename2)

for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
