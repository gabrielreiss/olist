import os
import sqlalchemy
import argparse
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) )
DATA_DIR = os.path.join( BASE_DIR, 'data' )
SQL_DIR = os.path.join( BASE_DIR, 'src', 'sql' )

# Abrindo conexão com banco...
user = 'olistado'
psw = '1234'
host = 'localhost'
port = '3306'
database = 'olist'

str_connection = 'mysql+pymysql://{user}:{psw}@{host}:{port}/{database}'
str_connection = str_connection.format( user=user, psw=psw, host=host, port=port, database = database )
engine = sqlalchemy.create_engine( str_connection )
connection = engine.connect()

#importa query
with open( os.path.join(SQL_DIR, 'teste.sql') ) as query_file:
    query = query_file.read()


tabela = pd.read_sql_query( query, connection)
print(tabela.head())