# pcost.py
#
# Exercise 1.27

def get_a_stock(): 
    with open('Data/portfolio.csv', 'rt') as f:
        next(f)
        for line in f:
            line = line.strip()
            line = line.split(',')
            yield line

total_cost = 0

for _, n_stock, stock_price in get_a_stock():
    # print(n_stock, stock_price)
    total_cost += int(n_stock) * float(stock_price)

print('Total Cost ', total_cost)




