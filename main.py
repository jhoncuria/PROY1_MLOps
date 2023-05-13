import pandas as pd
import numpy as np
from fastapi import FastAPI



app = FastAPI()

df = pd.read_csv("..//movies_clean1.csv")
#--------------------------------------------------------------------------------------------------



@app.get('/peliculas_mes/{mes}')
def peliculas_mes(mes: str):
    '''Se ingresa el mes y la función retorna la cantidad de películas que se estrenaron ese mes históricamente'''
    df_mes = df[df['month'] == mes]
    cantidad = len(df_mes)
    return {'mes': mes, 'cantidad': cantidad}




@app.get('/peliculas_dia/{dia}')
def peliculas_dia(dia: str):
    '''Se ingresa el día y la función retorna la cantidad de películas que se estrenaron ese día históricamente'''
    df_dia = df[df['day'] == dia]
    cantidad = len(df_dia)
    return {'dia': dia, 'cantidad': cantidad}

@app.get('/franquicia/{franquicia}')
def franquicia(franquicia: str):
    '''Se ingresa la franquicia, retornando la cantidad de películas, ganancia total y promedio'''
    df_franquicia = df[df['belongs_to_collection'] == franquicia]
    cantidad = len(df_franquicia)
    ganancia_total = df_franquicia['revenue'].sum()
    ganancia_promedio = df_franquicia['revenue'].mean()
    return {'franquicia': franquicia, 'cantidad': cantidad, 'ganancia_total': ganancia_total, 'ganancia_promedio': ganancia_promedio}

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais: str):
    '''Ingresas el país, retornando la cantidad de películas producidas en el mismo'''
    df_pais = df[df['production_countries'].apply(lambda x: pais in str(x))]
    cantidad = len(df_pais)
    return {'pais': pais, 'cantidad': cantidad}

@app.get('/productoras/{productora}')
def productoras(productora: str):
    '''Ingresas la productora, retornando la ganancia total y la cantidad de películas que produjeron'''
    df_productora = df[df['production_companies'].apply(lambda x: productora in str(x))]
    cantidad = len(df_productora)
    ganancia_total = df_productora['revenue'].sum()
    return {'productora': productora, 'ganancia_total': ganancia_total, 'cantidad': cantidad}



@app.get("/retorno/{pelicula}")
def retorno(pelicula: str):
    '''Ingresas la película, retornando la inversión, la ganancia, el retorno y el año en el que se lanzó'''
    df_filtrado = df[df['title'].apply(lambda x: pelicula.strip() == str(x.strip()))]
    inversion = df_filtrado["budget"].sum()
    ganancia = df_filtrado["revenue"].sum()
    retorno = df_filtrado["return"].sum()
    anio = pd.to_datetime(df_filtrado["year"]).dt.year

    return {'pelicula': pelicula, 'inversion': str(inversion), 'ganancia': str(ganancia), 'retorno': str(retorno), 'año':str(anio.item())}
