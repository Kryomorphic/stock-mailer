from . import stock
from db.operations import add_sub, remove_sub
from flask import request, abort, redirect


@stock.route('/sub', methods=['POST'])
def sub():
    if not request.form.get('phone_number') or not request.form.get('stock_ticker'):
        print('To add or remove a sub a phone number and a stock ticker value is required')
        abort(400)
    phone_number = request.form.get('phone_number')
    stock_ticker = request.form.get('stock_ticker')
    if request.form.get('remove') == 'True':
        remove_sub(stock_ticker, phone_number)
    else:
        add_sub(stock_ticker, phone_number)
    return redirect('/')

