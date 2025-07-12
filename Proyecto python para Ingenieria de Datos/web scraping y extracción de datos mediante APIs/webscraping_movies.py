print("El script webscraping_movies.py ha comenzado su ejecución.")
# Import necessary libraries
import os
import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

# Inicialización de entidades conocidas
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = '/home/miguel-oscar/DS_IBM_Course/DS_IBM_Course/Proyecto python para Ingenieria de Datos/web scraping y extracción de datos mediante APIs/top_50_films.csv'
df = pd.DataFrame(columns=["Average Rank","Film","Year"])
count = 0

# Cargando la página web para Webscraping
html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

# Extracción de información requerida
tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

# Iterar sobre las filas para encontrar los datos requeridos
for row in rows:
    if count<50:
        col = row.find_all('td')
        if len(col)!=0:
            data_dict = {"Average Rank": col[0].contents[0],
                         "Film": col[1].contents[0],
                         "Year": col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1], ignore_index=True)
            count+=1
    else:
        break
    
print(df)

# Almacenando los datos
df.to_csv(csv_path)

# Almacenar los datos requeridos en una base de datos
conn = sqlite3.connect(db_name) # Inicializar una conexión a la base de datos
df.to_sql(table_name, conn, if_exists='replace', index=False) #guardar el df como una tabla
conn.close() # Cerrar la conexión

