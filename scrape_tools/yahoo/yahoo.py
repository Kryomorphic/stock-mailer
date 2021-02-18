import requests
from bs4 import BeautifulSoup


def scrape_stock_price(stock_ticker):
    stock_page = requests.get('https://finance.yahoo.com/quote/{}'.format(stock_ticker))
    if stock_page.status_code != 200:
        print('encountered error when fetching yahoo page for stock {}'.format(stock_ticker))
        return None
    soup = BeautifulSoup(stock_page.text, 'html.parser')
    stock_price_span = soup.find_all('span', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})
    if len(stock_price_span) < 1 and len(stock_price_span[0].contents) < 1:
        print('unable to find price value on yahoo page for stock {}'.format(stock_ticker))
        return None
    else:
        return stock_price_span[0].contents[0]