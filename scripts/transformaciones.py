# Importacion de librerias
import pandas as pd
import numpy as np
import ast

#--------------------------------------------------------------------------------------------------

# Carga de datos
#ruta = os.path.join('..', 'datasets', 'movies_dataset.csv')
#df = pd.read_csv(ruta)
# df = pd.read_csv(r'C:\Users\sramr\OneDrive\Desktop\PI01_DTS10\datasets\movies_dataset.csv')

df = pd.read_csv("..//datasets//movies_dataset.csv")

#--------------------------------------------------------------------------------------------------

# Algunos campos, como belongs_to_collection, production_companies y otros (ver diccionario de datos)
# están anidados, esto es o bien tienen un diccionario o una lista como valores en cada fila, ¡deberán 
# desanidarlos para poder y unirlos al dataset de nuevo hacer alguna de las consultas de la API! O bien 
# buscar la manera de acceder a esos datos sin desanidarlos.

#--------------------------------------------------------------------------------------------------
def fetch_name(obj): 
    if isinstance(obj, str) and '{' in obj:
        L=[]
        for i in ast.literal_eval(obj):
            L.append(i['name']);
        return L

def fetch_name2(obj): 
        if isinstance(obj, str) and '{' in obj:
        # print(obj)
            dic = ast.literal_eval(obj)
            return dic['name']

df['genres'] = df['genres'].apply(fetch_name)
df['belongs_to_collection'] = df['belongs_to_collection'].apply(fetch_name2)
df['production_companies']  = df['production_companies'].apply(fetch_name)
df['production_countries']  = df['production_countries'].apply(fetch_name)
df['spoken_languages'] = df['spoken_languages'].apply(fetch_name)



# Los valores nulos de los campos revenue, budget deben ser rellenados por el número 0.
df = fillna_revenue_and_budget(df)

df['revenue'] = df['revenue'].fillna(0)
df['budget'] = df['budget'].fillna(0)

#--------------------------------------------------------------------------------------------------

# Los valores nulos del campo release date deben eliminarse.
df = dropna_release_date(df)

df.dropna(subset=['release_date'], inplace=True)

# Convertir la columna release_date en formato datetime
df['release_date'] = pd.to_datetime(df["release_date"], format='%Y-%m-%d', errors = 'coerce')
df ['release_date'].dropna(inplace=True)
mascara = df[df["release_date"].isnull()]
df = df.drop(labels= mascara.index, axis=0)
# Crear las columnas separadas para año, mes y día:
df['release_year'] = df['release_date'].dt.year
df['release_month'] = df['release_date'].dt.month
df['release_day'] = df['release_date'].dt.day

# Establecer la configuración regional en español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
df["year"] = df['release_year']
df["month"] = df['release_date'].dt.strftime('%B').apply(lambda x: x.capitalize() if type(x) != float else x)
df["day"] = df['release_date'].dt.strftime('%A').apply(lambda x: x.capitalize() if type(x) != float else x)



#--------------------------------------------------------------------------------------------------

# Crear la columna con el retorno de inversión, llamada return con los campos revenue y budget,
# dividiendo estas dos últimas revenue / budget, cuando no hay datos disponibles para calcularlo, 
# deberá tomar el valor 0.
df = add_inversion_column(df)

# Limpiar y convertir a numérico las columnas revenue y budget

df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce').fillna(0)
df['budget'] = pd.to_numeric(df['budget'], errors='coerce').fillna(0)

# Calcular el return

df['return'] = np.where(df['budget'] > 0, df['revenue'] / df['budget'], 0)
df['return'] = df['return'].apply(lambda x: round(x, 2))



#--------------------------------------------------------------------------------------------------

# Eliminar las columnas que no serán utilizadas, video,imdb_id,adult,original_title,vote_count,
# poster_path y homepage.
df = drop_useless_columns(df)

# Eliminacion de columnas
df = df.drop(['video', 'imdb_id', 'adult', 'original_title', 'vote_count', 'poster_path', 'homepage', 'release_year', 'release_month', 'release_day',], axis=1)


#--------------------------------------------------------------------------------------------------


# df.to_csv('movies_etl.csv', index=False, encoding='utf-8')
