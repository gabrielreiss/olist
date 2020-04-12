import os
import sqlalchemy
import argparse
import pandas as pd


# Os endereços de nosso projeto e sub pastas
BASE_DIR = os.path.dirname(os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) )
DATA_DIR = os.path.join( BASE_DIR, 'data' )
SQL_DIR = os.path.join( BASE_DIR, 'src', 'sql' )


#con.query('SET GLOBAL connect_timeout=6000')

with open( os.path.join(SQL_DIR, 'segmentos.sql') ) as query_file:
    query = query_file.read()

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

