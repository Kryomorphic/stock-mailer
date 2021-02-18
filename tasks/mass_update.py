from db.operations import get_subs
from mailer_tools import send_message
import scrape_tools.yahoo as yahoo
import time


def mass_update():
    counter = 0
    subscriptions = get_subs(counter, 10)
    stock_dict = {}
    while len(subscriptions) > 0:
        for sub in subscriptions:
            if sub.stock_ticker not in stock_dict:
                stock_dict[sub.stock_ticker] = yahoo.scrape_stock_price(sub.stock_ticker)
                time.sleep(1.0)
            send_message(sub.phone_number, '{}: {}'.format(sub.stock_ticker, stock_dict[sub.stock_ticker]))
        counter += 10
        subscriptions = get_subs(counter, 10)
