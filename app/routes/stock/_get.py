from . import stock
from flask import render_template
from db.operations import get_subs


@stock.route('/', methods=['GET'])
def index():
    subs = get_subs(None, None)
    print(subs)
    return render_template('index.html', subs=subs)

