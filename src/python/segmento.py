import os
import sqlalchemy
import argparse
import pandas as pd


# Os endereços de nosso projeto e sub pastas
BASE_DIR = os.path.dirname(os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) )
DATA_DIR = os.path.join( BASE_DIR, 'data' )
SQL_DIR = os.path.join( BASE_DIR, 'src', 'sql' )

parser = argparse.ArgumentParser()
parser.add_argument( '--date_init', '-i', help='Data de inicio da extração', default= '2017-06-01' )
parser.add_argument( '--date_end', '-e', help='Data de inicio da extração', default= '2018-06-01' )
args = parser.parse_args()

data = '2018-06-01'

#con.query('SET GLOBAL connect_timeout=6000')

#importa query
with open( os.path.join(SQL_DIR, 'segmentos.sql') ) as query_file:
    query = query_file.read()

query = query.format( date_init = args.date_init,
                      date_end = args.date_end   )

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

create_query = f'''
CREATE TABLE tb_seller_sgmt AS
{query}
;'''

insert_query = f'''
DELETE FROM tb_seller_sgmt WHERE DT_SGMT ='{args.date_end}';
INSERT INTO tb_seller_sgmt
{query}
;'''

try:
    connection.execute( create_query )
except:
    for q in insert_query.split(";")[:-1]:
        connection.execute( insert_query )





#df = pd.read_sql_query( query, connection )
#print(df)