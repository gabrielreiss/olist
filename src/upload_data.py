import os
import pandas as pd
import sqlalchemy
import pymysql

user = 'olistado'
psw = '1234'
host = 'localhost'
port = '3306'
database = 'olist'

# Os endereços de nosso projeto e sub pastas
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
DATA_DIR = os.path.join( BASE_DIR, 'data' )

# Encontrando os arquivos de dados
files_names = [ i for i in os.listdir( DATA_DIR ) if i.endswith('.csv') ]

# Abrindo conexão com banco...
str_connection = 'mysql+pymysql://{user}:{psw}@{host}:{port}/{database}'.format(user=user, psw=psw, host=host, port=port, database = database)
#str_connection = str_connection.format( user=user, psw=psw, host=host, port=port )
engine = sqlalchemy.create_engine( str_connection )
connection = engine.connect()


def data_quality(x):
    if type(x) == str:
        return x.replace("\n", "").replace("\r", '')
    else:
        return x

# Para cada arquivo é realizado uma inserção no banco
for i in files_names:
    print(i)
    df_tmp = pd.read_csv( os.path.join( DATA_DIR, i )  )
    for c in df_tmp.columns:
        df_tmp[c] = df_tmp[c].apply(data_quality)
    
    table_name = "tb_" + i.strip(".csv").replace("olist_", "").replace("_dataset", "")
    #print(df_tmp.head())
    df_tmp.to_sql( table_name,
                   connection,
                   schema = 'olist',
                   if_exists='replace',
                   index=False )