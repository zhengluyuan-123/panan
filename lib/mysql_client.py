import logging
import warnings
import pandas as pd
import pymysql
from sqlalchemy import create_engine

# 利用过滤器来实现忽略告警
warnings.filterwarnings('ignore')

format = '%(asctime)s-%(name)s-%(message)s'
logging.basicConfig(level=logging.INFO, format=format)


class Mysql(object):

    def __init__(self, host=None, port=None, user=None, password=None, db=None):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db

    def create_engine(self):
        return create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
            self.user, self.port, self.user, self.password, self.db))

    def get_cur(self):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                               password=self.password, db=self.db)
        return conn

    def execute_sql(self, sql):
        conn = self.get_cur()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
            return cur.fetchall()

        except Exception as e:
            conn.rollback()
            raise (e)
        finally:
            cur.close()
            conn.close()

    def execute_sql_list(self, sql):
        conn = self.get_cur()
        cur = conn.cursor()
        try:
            for i in sql:
                cur.execute(sql)
            conn.commit()
            return cur.fetchall()

        except Exception as e:
            conn.rollback()
            raise (e)
        finally:
            cur.close()
            conn.close()

    def executemany_sql(self,sql):
        conn = self.get_cur()
        cur = conn.cursor()
        try:
            cur.executemany(sql)
            conn.commit()
            return cur.fetchall()

        except Exception as e:
            conn.rollback()
            raise (e)
        finally:
            cur.close()
            conn.close()

    def read_table(self, table_name, index_col=None):
        data = pd.read_sql_table(table_name, con=self.create_engine(), index_col=index_col)
        return data


def get_db(db):

    if 1==1:
        if db == 'pasms':
            sql_host = '30.99.140.185'
            sql_port = 3306
            sql_user = 'deployop'
            sql_password = 'Paic12345'
            sql_database = 'pasms'
        else:
            sql_host = '30.99.140.185'
            sql_port = 3306
            sql_user = 'deployop'
            sql_password = 'Paic12345'
            sql_database = 'pasms'
    return Mysql(host=sql_host,  port=sql_port, user=sql_user,
                 password=sql_password, db=sql_database)


db_mysql = get_db('pasms')

if __name__ == "__main__":
    pass