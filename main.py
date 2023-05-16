import pandas as pd
import numpy as np
from fastapi import FastAPI


df = pd.read_csv("..//Proy_Ind_1_final//datasets//movies_etl.csv")
df = pd.read_csv("..//Proy_Ind_1_final//datasets//movies_ml.csv")

app = FastAPI()

@app.get("/")
async def index():
    return {'PROYECTO INDIVIDUAL MLOps SOYHENRY'}

@app.get("/")
async def index():
    return {'Ejecutar '}

#--------------------------------------------------------------------------------------------------

# Funcion  1

@app.get('/peliculas_mes/{mes}')
def peliculas_mes(mes: str):
    '''Se ingresa el mes y la función retorna la cantidad de películas que se estrenaron ese mes históricamente'''
    df_mes = df[df['month'] == mes]
    cantidad = len(df_mes)
    return {'mes': mes, 'cantidad': cantidad}


# Funcion 2

@app.get('/peliculas_dia/{dia}')
def peliculas_dia(dia: str):
    '''Se ingresa el día y la función retorna la cantidad de películas que se estrenaron ese día históricamente'''
    df_dia = df[df['day'] == dia]
    cantidad = len(df_dia)
    return {'dia': dia, 'cantidad': cantidad}

# Funcion 3

@app.get('/franquicia/{franquicia}')
def franquicia(franquicia: str):
    '''Se ingresa la franquicia, retornando la cantidad de películas, ganancia total y promedio'''
    df_franquicia = df[df['belongs_to_collection'] == franquicia]
    cantidad = len(df_franquicia)
    ganancia_total = df_franquicia['revenue'].sum()
    ganancia_promedio = df_franquicia['revenue'].mean()
    return {'franquicia': franquicia, 'cantidad': cantidad, 'ganancia_total': ganancia_total, 'ganancia_promedio': ganancia_promedio}

# Funcion 4

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais: str):
    '''Ingresas el país, retornando la cantidad de películas producidas en el mismo'''
    df_pais = df[df['production_countries'].apply(lambda x: pais in str(x))]
    cantidad = len(df_pais)
    return {'pais': pais, 'cantidad': cantidad}

# Funcion 5

@app.get('/productoras/{productora}')
def productoras(productora: str):
    '''Ingresas la productora, retornando la ganancia total y la cantidad de películas que produjeron'''
    df_productora = df[df['production_companies'].apply(lambda x: productora in str(x))]
    cantidad = len(df_productora)
    ganancia_total = df_productora['revenue'].sum()
    return {'productora': productora, 'ganancia_total': ganancia_total, 'cantidad': cantidad}

# Funcion 6

@app.get("/retorno/{pelicula}")
def retorno(pelicula: str):
    '''Ingresas la película, retornando la inversión, la ganancia, el retorno y el año en el que se lanzó'''
    df_filtrado = df[df['title'].apply(lambda x: pelicula.strip() == str(x.strip()))]
    inversion = df_filtrado["budget"].sum()
    ganancia = df_filtrado["revenue"].sum()
    retorno = df_filtrado["return"].sum()
    anio = pd.to_datetime(df_filtrado["year"]).dt.year

    return {'pelicula': pelicula, 'inversion': str(inversion), 'ganancia': str(ganancia), 'retorno': str(retorno), 'año':str(anio.item())}

# Funcion ML


data = data.drop_duplicates(subset = 'title')
C = data['vote_average'].mean()
m = data['vote_count'].quantile(0.90)
m = data['vote_count'].quantile(0.90)
data = data.loc[data['vote_count'] >= m]
def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    # Calculation based on the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)
data['score'] = data.apply(weighted_rating, axis=1)
data = data.sort_values('score', ascending = False)
tfidf = TfidfVectorizer(stop_words='english')
data['overview'] = data['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(data['overview'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
data.reset_index(drop = True, inplace = True)
index = pd.Series(data.index, index = data['title']).drop_duplicates()

# Funcion de recomendacion 

@app.get("/recomendacion/{pelicula}")
def recomendacion(titulo, cosine_sim = cosine_sim):
    if titulo not in index:
    return "La película no se encuentra entre el 10% de las mejores películas. Intenta con una mejor!"

    idx = index[titulo]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse = True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    result = data['title'].iloc[movie_indices]
    return {"Te recomendamos estas peliculas" : list(result)}








