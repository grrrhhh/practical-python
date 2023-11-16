# fileparse.py
#
# Exercise 3.3
# fileparse.py
import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(lines, delimiter=delimiter)
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
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", row_no, row)
                    log.debug("Row %d: Reason %s", row_no, e)
                continue
        
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)

        records.append(record)
    
    return records

if __name__ == '__main__':
    import gzip
    with gzip.open('Data/portfolio.csv.gz', 'rt') as file:
        port = parse_csv(file, types=[str,int,float])

    print(port)

    lines = ['name,shares,price','AA,100,34.23','IBM,50,91.1','HPE,75,45.1']
    port1 = parse_csv(lines, types=[str,int,float])
    print(port1)


    with open('Data/portfolio.csv', 'rt') as file:
        port2 = parse_csv(file, types=[str, int, float])

    print(port2)
