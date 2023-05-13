import pandas as pd
from pathlib import Path

file_path = Path("movies_data.csv")
movies = pd.read_csv(file_path)


def peliculas_mes(mes):
    count = movies[movies['mes'] == mes].shape[0]
    return {'mes': mes, 'cantidad': count}


def peliculas_dia(dia):
    count = movies[movies['dia'] == dia].shape[0]
    return {'dia': dia, 'cantidad': count}


def franquicia(franquicia):
    count = movies[movies['franquicia'] == franquicia].shape[0]
    ganancia_total = movies[movies['franquicia'] == franquicia]['ganancia'].sum()
    ganancia_promedio = movies[movies['franquicia'] == franquicia]['ganancia'].mean()
    return {'franquicia': franquicia, 'cantidad': count, 'ganancia_total': ganancia_total, 'ganancia_promedio': ganancia_promedio}


def peliculas_pais(pais):
    count = movies[movies['pais'] == pais].shape[0]
    return {'pais': pais, 'cantidad': count}


def productoras(productora):
    count = movies[movies['productora'] == productora].shape[0]
    ganancia_total = movies[movies['productora'] == productora]['ganancia'].sum()
    return {'productora': productora, 'ganancia_total': ganancia_total, 'cantidad': count}


def retorno(pelicula):
    pelicula_data = movies[movies['pelicula'] == pelicula].iloc[0]
    inversion = pelicula_data['inversion']
    ganancia = pelicula_data['ganancia']
    retorno = ganancia / inversion
    anio = pelicula_data['anio']
    return {'pelicula': pelicula, 'inversion': inversion, 'ganancia': ganancia, 'retorno': retorno, 'anio': anio}