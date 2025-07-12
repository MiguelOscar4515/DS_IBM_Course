import pandas as pd
import sqlite3

conn = sqlite3.connect('STAFF.db')

table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

file_path = '/home/miguel-oscar/DS_IBM_Course/DS_IBM_Course/Proyecto python para Ingenieria de Datos/web scraping y extracción de datos mediante APIs/INSTRUCTOR.csv'

df = pd.read_csv(file_path, names=attribute_list)

df.to_sql(table_name, conn, if_exists='replace', index=False)
print('Table is ready for use')

query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

conn.close()