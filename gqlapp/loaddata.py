import sqlite3
import pandas as pd

conn = sqlite3.connect('/Users/mpran/PycharmProjects/graphexample/db.sqlite3')

df = pd.read_csv('/Users/mpran/PycharmProjects/graphexample/sam.csv')
df['id'] = df.index
df = df[[ 'id','Segment', 'Country', 'Product', 'Units', 'Sales', 'Datesold']]
df.to_sql('gqlapp_productmodel', conn, if_exists='replace', index=False)