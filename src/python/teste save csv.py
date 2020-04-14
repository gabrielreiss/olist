import os
import sqlalchemy
import argparse
import pandas as pd

# Os endereços de nosso projeto e sub pastas
BASE_DIR = os.path.dirname(os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) )
DATA_DIR = os.path.join( BASE_DIR, 'data' )
SQL_DIR = os.path.join( BASE_DIR, 'src', 'sql' )
RESULT_DIR = os.path.join( BASE_DIR, 'resultado' )

def consulta_bc(codigo_bcb):
  url = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json'.format(codigo_bcb)
  df = pd.read_json(url)
  df['data'] = pd.to_datetime(df['data'], dayfirst=True)
  df.set_index('data', inplace=True)
  return df

ipca = consulta_bc(433)

ipca.to_csv( os.path.join( RESULT_DIR, 'ipca.csv') )