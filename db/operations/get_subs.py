import db.models.RelationStockNumber as RelationStockNumber
from db.access import mysql_session


def get_subs(offset, limit):
    for i in range(3):
        try:
            q = mysql_session.query(RelationStockNumber).filter(RelationStockNumber.enabled == 1)
            if offset is not None:
                q = q.offset(offset)
            if limit is not None:
                q = q.limit(limit)
            result = q.all()
            return result
        except Exception as e:
            print('an error occurred while adding RelationStockNumber entry'
                  ' attempt number {}'.format(e, i + 1))
    return None
