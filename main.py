import pandas as pd
from fastapi import FastAPI

meses_esp = {
    'January': 'enero',
    'February': 'febrero',
    'March': 'marzo',
    'April': 'abril',
    'May': 'mayo',
    'June': 'junio',
    'July': 'julio',
    'August': 'agosto',
    'September': 'septiembre',
    'October': 'octubre',
    'November': 'noviembre',
    'December': 'diciembre'
}

dias_semana = {
    'Monday': 'Lunes',
    'Tuesday': 'Martes',
    'Wednesday': 'Miércoles',
    'Thursday': 'Jueves',
    'Friday': 'Viernes',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo'
}

app = FastAPI()

df = pd.read_csv(r'data_movies_corr.csv')
df['release_date'] = pd.to_datetime(df['release_date'], format='%Y-%m-%d')
df['month_release'] = df['release_date'].apply(lambda x: meses_esp[x.strftime('%B')])
df['day_of_week_release'] = df['release_date'].apply(lambda x: dias_semana[x.strftime('%A')])


@app.get('/peliculas_mes/{mes}')
def peliculas_mes(mes:str):
    '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes historicamente'''
    df_mes = df[df['month_release'] == mes]
    cantidad = len(df_mes)
    return {'mes': mes, 'cantidad': cantidad}


@app.get('/peliculas_dia/{dia}')
def peliculas_dia(dia:str):
    '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrebaron ese dia historicamente'''
    df_dia = df[df['day_of_week_release'] == dia]
    cantidad = len(df_dia)
    return {'dia': dia, 'cantidad': cantidad}

@app.get('/franquicia/{franquicia}')
def franquicia(franquicia:str):
    '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio'''
    franquicia_df = df[df['belongs_to_collection'].apply(lambda x: x is not None and x['name'] == franquicia)]
    cantidad = len(franquicia_df)
    ganancia_total = franquicia_df['revenue'].sum()
    ganancia_promedio = franquicia_df['revenue'].mean() if cantidad > 0 else 0
    return {'franquicia': franquicia, 'cantidad': cantidad, 'ganancia_total': ganancia_total, 'ganancia_promedio': ganancia_promedio}

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais:str):
    '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo'''
    pais_df = df[df['production_countries'].apply(lambda x: any(d['name'] == pais for d in x))]
    cantidad = len(pais_df)
    return {'pais': pais, 'cantidad': cantidad}

@app.get('/productoras/{productora}')
def productoras(productora:str):
    '''Ingresas la productora, retornando la ganancia toal y la cantidad de peliculas que produjeron'''
    productora_df = df[df['production_companies'].apply(lambda x: any(d['name'] == productora for d in x))]
    ganancia_total = productora_df['revenue'].sum()
    cantidad = productora_df['revenue'].count()
    return {'productora': productora, 'ganancia_total': ganancia_total, 'cantidad': cantidad}
@app.get('/retorno/{pelicula}')
def retorno(pelicula:str):
    '''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo'''
    pelicula_df = df.loc[df['title'] == pelicula]
    inversion = pelicula_df['budget'].values[0]
    ganancia = pelicula_df['revenue'].values[0]
    retorno = pelicula_df['return'].values[0]
    anio = pelicula_df['release_date'].dt.year.values[0]
    return {'pelicula':pelicula, 'inversion':inversion, 'ganacia':ganancia,'retorno':retorno, 'anio':anio}

# ML
@app.get('/recomendacion/{titulo}')
def recomendacion(titulo:str):
    '''Ingresas un nombre de pelicula y te recomienda las similares en una lista'''
    return {'lista recomendada': 'respuesta'}
