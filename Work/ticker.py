from follow import follow
import csv
import report
from tableformat import create_formatter, print_table


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows


def select_columns(rows, indices):
     for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    rows = (row for row in rows if row['name'] in names)
    return rows

def ticker(portfolio_file, logfile, fmt='txt'):
    portfolio = report.read_portfolio(portfolio_file)
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)

    formatter = create_formatter(fmt)
    formatter.headings(['Name','Price','Change'])
    for row in rows:
        formatter.row([ row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"] )


def main(args):
    if len(args) != 4:
        # raise SystemExit('Usage: %s portfoliofile logfile fmt' % args[0])
        ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'txt')
    else:
        ticker(args[1], args[2], args[3])


if __name__ == '__main__':
    import sys
    main(sys.argv)
