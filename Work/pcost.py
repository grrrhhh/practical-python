# pcost.py
#

import sys
import report

def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return sum( [s['shares']*s['price'] for s in portfolio] )

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)
