# report.py
#
# Exercise 2.4
import sys
from pprint import pprint 
import csv
import fileparse

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    
    portfolio = fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])
    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = dict(fileparse.parse_csv(filename,types=[str,float], has_headers=False))
    return prices

def make_report(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)    
    return rows



def print_report(report):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))

    for name, shares, price, change in report:
            print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')



def portfolio_report(portfoliofile, pricefile):
    '''
    Make a stock report given portfolio and price data files.
    '''

    #read data files
    portfolio = read_portfolio(portfoliofile)
    prices    = read_prices(pricefile)

    #create the report data
    report = make_report(portfolio, prices)

    #print the report
    print_report(report)

portfolio_report('Data/portfolio.csv','Data/prices.csv')