# pcost.py
#
# Exercise 1.27

total_cost = 0.0

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        print(row)
        nshares = int(row[1])
        price = float(row[2])
        total_cost= total_cost + nshares * price

    print('Total cost', total_cost)
       
