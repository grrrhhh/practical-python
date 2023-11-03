# fileparse.py
#
# Exercise 3.3
# fileparse.py
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        if has_headers:
            headers = next(rows)
            
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row_no, row in enumerate(rows, start=1):
            if not row:
                continue

            if indices:
                row = [ row[index] for index in indices ]
           
            if types:
                try:
                    row = [ func(val) for func, val in zip(types, row) ]
                except ValueError as e:
                    if silence_errors:
                        continue
                    print(f"Row {row_no}: Couldn't convert {row}")
                    print(f"Row {row_no}: {e}")
            
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)
    
    return records

portfolio = parse_csv('Data/portfolio.csv', types=[str, int, float])
shares_held = parse_csv('Data/portfolio.csv', select=['name', 'shares'], types=[str, int])
prices = parse_csv("Data/prices.csv", types=[str,float], has_headers=False)
portfolio_2 = portfolio = parse_csv('Data/portfolio.dat', types=[str, int, float], delimiter=' ')
portfolio = parse_csv('Data/missing.csv', types=[str, int, float])
portfolio = parse_csv('Data/missing.csv', types=[str,int,float], silence_errors=True)
