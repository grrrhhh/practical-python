# report.py
#
from fileparse import parse_csv

def read_portfolio(filename):
    with open(filename, 'rt') as lines:
        portfolio = parse_csv(lines, types=[str, int, float])
    return portfolio

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    total = 0.0
    for holding in portfolio:
        total += holding['shares'] * holding['price']
    return total

def read_prices(filename):
    with open(filename) as lines:
        ticker = dict(parse_csv(lines, types=[str,float], has_headers=False)) 
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

def make_report(portfolio, ticker):
    report = []

    for holding in portfolio:
        symbol = holding['name']
        change_in_price = ticker[symbol] - holding['price']
        row = ( symbol, holding['shares'], ticker[symbol], change_in_price )
        report.append(row)
    return report

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))

    for name, shares, price, change in report:
        price = "$" + f'{price:.2f}'
        print(f"{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}")


def portfolio_report(f_portfolio, f_prices):
    portfolio = read_portfolio(f_portfolio)
    prices = read_prices(f_prices)
    print_report(make_report(portfolio, prices))

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])

    portfolio_source, price_source = args[1], args[2]
    portfolio = read_portfolio(portfolio_source)
    prices = read_prices(price_source)

    print('Portfolio Cost: ', portfolio_cost(portfolio_source) )
    print('P/L:', calculate_p_l(portfolio, prices) )

    portfolio_report(portfolio_source, price_source)

if __name__ == '__main__':
    import sys
    main(sys.argv)
