import db.models.RelationStockNumber as RelationStockNumber
from db.access import mysql_session


def add_sub(stock_ticker, phone_number):
    for i in range(3):
        try:
            q = mysql_session.query(RelationStockNumber) \
                .filter(RelationStockNumber.stock_ticker == stock_ticker) \
                .filter(RelationStockNumber.phone_number == phone_number)
            result = q.all()
            if len(result) > 0:
                q.update({'enabled': 1})
                mysql_session.commit()
            else:
                new_relation = RelationStockNumber(stock_ticker=str(stock_ticker), phone_number=str(phone_number), enabled=1)
                mysql_session.add(new_relation)
                mysql_session.commit()
            return True
        except Exception as e:
            print('an error occurred while adding RelationStockNumber entry'
                  ' attempt number {}'.format(e, i + 1))
    return None
