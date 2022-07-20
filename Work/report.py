# report.py
#
# Exercise 2.12
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
    Reads a CSV file of price data and returns a dictionary with keys: name, price
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
    Make a list of (name, shares, price, change) tuples given a portfolio list and prices dictionary.
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


# Read data files an create the report data
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

# Generate the report data
report = make_report(filename, filename2)

# Output the report
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {f"${price:0.2f}":>10s} {change:>10.2f}')
