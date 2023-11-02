# report.py
#
# Exercise 2.4
import csv
from pprint import pprint

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            holding = { headers[i]: row[i] for i in range(len(headers)) }
            holding['shares'] = int(holding['shares'])
            holding['price'] = float(holding['price'])
            portfolio.append(holding)

    return portfolio

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    total = 0.0

    for holding in portfolio:
        total += holding['shares'] * holding['price']

    return total

def read_prices(filename):
   
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        ticker = { row[0]: float(row[1])  for row in rows if row}

    return ticker


def calculate_p_l(portfolio, ticker):
    current_portfolio_value = 0.0
    ungained_portfolio_value = 0.0

    for holding in portfolio:
        symbol = holding['name']
        current_price = ticker[symbol] * holding['shares']
        current_portfolio_value += current_price
        ungained_portfolio_value += holding['price'] * holding['shares']

    p_l = current_portfolio_value - ungained_portfolio_value

    return p_l

portfolio_source = 'Data/portfolio.csv'
price_source = 'Data/prices.csv'

portfolio = read_portfolio(portfolio_source)
pprint(portfolio)

prices = read_prices(price_source)
pprint(prices)

print('Portfolio Cost: ', portfolio_cost(portfolio_source) )
print('P/L:', calculate_p_l(portfolio, prices) )

