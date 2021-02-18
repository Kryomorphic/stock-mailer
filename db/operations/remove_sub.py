import db.models.RelationStockNumber as RelationStockNumber
from db.access import mysql_session


def remove_sub(stock_ticker, phone_number):
    for i in range(3):
        try:
            mysql_session.query(RelationStockNumber) \
                .filter(RelationStockNumber.stock_ticker == stock_ticker) \
                .filter(RelationStockNumber.phone_number == phone_number) \
                .update({'enabled': 0})
            mysql_session.commit()
            return True
        except Exception as e:
            print('an error occurred while disabling RelationStockNumber entry'
                  ' attempt number {}'.format(e, i + 1))
    return None
