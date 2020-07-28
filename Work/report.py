# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                 'name'   : record['name'],
                 'shares' : int(record['shares']),
                 'price'   : float(record['price'])
            }
            portfolio.append(stock)

    return portfolio

def read_prices(filename):
    
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

def make_report(portfolio, prices):
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)    
    return rows



def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))

    for name, shares, price, change in report:
            print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')



def portfolio_report(portfoliofile, pricefile):

    #read data files
    portfolio = read_portfolio(portfoliofile)
    prices    = read_prices(pricefile)

    #create the report data
    report = make_report(portfolio, prices)

    #print the report
    print_report(report)

portfolio_report('Data/portfolio.csv','Data/prices.csv')