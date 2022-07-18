# report.py
#
# Exercise 2.6
import csv

def read_portfolio(filename):
    '''
    Reads a stock portfolio file and returns a list of dictionaries of the 
portfolio file with keys: name, shares, price
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
