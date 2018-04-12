from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
from datetime import date

engine = create_engine(
    'postgresql://postgres:postgres@postgres.clz6zjqwa716.us-west-2.rds.amazonaws.com:5432/pedidos', echo=True)


def insert(obj):
    sess = Session(bind=engine)
    sess.add(obj)
    sess.commit()


def delete(obj):
    sess = Session(bind=engine)
    sess.delete(obj)
    sess.commit()


def update(obj):
    sess = Session(bind=engine)
    sess.merge(obj)
    sess.commit()


def find_all(cls):
    sess = Session(bind=engine)
    resp = sess.query(cls).all()
    sess.close()
    return resp
