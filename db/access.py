import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.automap import automap_base

load_dotenv('./.env')


def db_init(uri):
    engine = create_engine(uri,
                           echo=False,
                           isolation_level='READ_COMMITTED',
                           pool_size=20,
                           max_overflow=10,
                           pool_pre_ping=True,
                           pool_recycle=500)
    session = scoped_session(sessionmaker(bind=engine, autoflush=False, expire_on_commit=False))
    base = automap_base()
    base.prepare(engine, reflect=True)
    return engine, session, base


mysql_uri = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
    os.environ.get('MYSQL_USER'),
    os.environ.get('MYSQL_PASSWORD'),
    os.environ.get('MYSQL_HOST'),
    os.environ.get('MYSQL_PORT'),
    os.environ.get('MYSQL_DB')
)

mysql_engine, mysql_session, mysql_base = db_init(mysql_uri)
