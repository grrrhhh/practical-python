# report.py
#
from fileparse import parse_csv
from stock import Stock
from portfolio import Portfolio
import tableformat 

def read_portfolio(filename):
    with open(filename, 'rt') as lines:
        portfolio = parse_csv(lines, types=[str, int, float])

    portfolio = [ Stock(h['name'], h['shares'], h['price']) for h in portfolio]
    return Portfolio(portfolio)

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    total = 0.0
    for holding in portfolio:
        total += holding.shares * holding.price
    return total

def read_prices(filename):
    with open(filename) as lines:
        ticker = dict(parse_csv(lines, types=[str,float], has_headers=False)) 
    return ticker


def calculate_p_l(portfolio, ticker):
    current_portfolio_value = 0.0
    ungained_portfolio_value = 0.0

    for holding in portfolio:
        symbol = holding.name
        current_price = ticker[symbol] * holding.shares
        current_portfolio_value += current_price
        ungained_portfolio_value += holding.price * holding.shares

    p_l = current_portfolio_value - ungained_portfolio_value
    return p_l

def make_report(portfolio, ticker):
    report = []

    for holding in portfolio:
        symbol = holding.name
        change_in_price = ticker[symbol] - holding.price
        row = ( symbol, holding.shares, ticker[symbol], change_in_price )
        report.append(row)
    return report

def print_report(report, formatter):
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)


def portfolio_report(f_portfolio, f_prices, fmt='txt'):
    portfolio = read_portfolio(f_portfolio)
    prices = read_prices(f_prices)
    report = make_report(portfolio, prices)

    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile report_format' % args[0])

    portfolio_source, price_source, fmt = args[1], args[2], args[3]
    portfolio = read_portfolio(portfolio_source)
    prices = read_prices(price_source)

    print('Portfolio Cost: ', portfolio_cost(portfolio_source) )
    print('P/L:', calculate_p_l(portfolio, prices) )

    portfolio_report(portfolio_source, price_source, fmt)

if __name__ == '__main__':
    import sys
    main(sys.argv)
