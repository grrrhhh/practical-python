class TableFormatter:
    def headings(self, headers):
	    raise NotImplementedError()

    def row(self, rowdata):
	    raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        table_headers = ['<tr>']
        for h in headers:
            table_headers.append(f'<th>{h}</th>')
        table_headers.append('</tr>')
        print(''.join(table_headers))

    def row(self, rowdata):
        table_row = ['<tr>']
        for column in rowdata:
            table_row.append(f'<td>{column}</td>')
        table_row.append('</tr>')
        print(''.join(table_row))


class FormatError(Exception):
    pass

def create_formatter(fmt):
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {fmt}') 
    
    return formatter


def print_table(table, columns, formatter):
    formatter.headings(columns)
    for row in table:
        rowdata = [ str(getattr(row, col_name)) for col_name in columns ]
        formatter.row(rowdata)


