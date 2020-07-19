# pcost.py
#
# Exercise 1.27
import csv

def portfolio_cost(filename):

    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:   
                nshares = int(row[1])
                price = float(row[2])
                total_cost= total_cost + nshares * price

            except ValueError:
                print('Bad row', row)
    
    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost', cost)
       
