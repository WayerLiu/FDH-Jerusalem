import pandas as pd
from sqlalchemy import create_engine


# def Df_to_sql(df, name, db, psw, user='root', ip='localhost'):
#     '''
#     :param df: The data to pass
#     :param name: The name of the table in db
#     :param psw: Your password of your database
#     :param ip: Your IP
#     :param db: The name of your database
#     :param user: root
#     :return: None
#     '''


# con = create_engine('mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE))
df = pd.read_csv('total_list_permatch_3.0.csv')
#
# con = create_engine('mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE))  # mysql+pymysql的意思为：指定引擎为pymysql
# df.to_sql("neighbor_list", con)


import pymysql
import pandas as pd
from sqlalchemy import create_engine
#Start connection.
conn = create_engine('mysql+pymysql://root:12345678@localhost:3306/neighbor',encoding='utf8')

pd.io.sql.to_sql(df, "neighbor_total_list", conn, if_exists='replace')
