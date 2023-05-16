# PROYECTO INDIVIDUAL MLOps
El Proyecto Individual  de MLOps consiste en desarrollar un sistema de recomendación para una startup de agregación de plataformas de streaming. Se requiere realizar transformaciones de datos, desarrollar una API con consultas específicas, implementar el modelo en un servicio de deployment, realizar análisis exploratorio de los datos, y entrenar un modelo de machine learning para recomendar películas basado en similitudes. Además, se debe generar un video para demostrar los resultados del proyecto.


![](https://www.techies.es/wp-content/uploads/2020/09/netflix-wallpaper-1024x674.jpeg)
![](https://img.shields.io/github/stars/pandao/editor.md.svg) ![](https://img.shields.io/github/forks/pandao/editor.md.svg) ![](https://img.shields.io/github/tag/pandao/editor.md.svg) ![](https://img.shields.io/github/release/pandao/editor.md.svg) ![](https://img.shields.io/github/issues/pandao/editor.md.svg) ![](https://img.shields.io/bower/v/editor.md.svg)


## Introducción/Objetivo del proyecto

El Proyecto Individual se centra en el desarrollo de MLOps (Machine Learning Operations) para implementar un sistema de recomendación en una startup de servicios de agregación de plataformas de streaming. A continuación, se resumen los principales puntos del proyecto:

Transformaciones de datos: Se requiere realizar transformaciones rápidas en los datos, que incluyen desanidar campos anidados, rellenar valores nulos en campos de revenue y budget con ceros, eliminar valores nulos en el campo de release date, formatear fechas en el formato AAAA-mm-dd y crear la columna de retorno de inversión.

Desarrollo de API: Se propone disponibilizar los datos de la empresa a través del framework FastAPI. Se deben crear seis funciones de endpoints que permitan realizar consultas a la API, como obtener la cantidad de películas estrenadas en un mes o día específico, obtener información de una franquicia, obtener la cantidad de películas producidas en un país, obtener información de una productora y obtener información de retorno para una película.

Deployment: Se sugiere utilizar servicios como Render o Railway para implementar la API y permitir que sea consumida desde la web, en este caso se uso Render.

Análisis exploratorio de datos (EDA): Se debe realizar un análisis exploratorio de los datos limpios, investigando las relaciones entre las variables, identificando outliers o anomalías, y explorando patrones interesantes. Se mencionan algunas librerías como pandas profiling, missingno, sweetviz y autoviz para realizar el análisis.

Sistema de recomendación: Una vez que los datos están disponibles a través de la API y se ha realizado el EDA, se debe entrenar un modelo de machine learning para construir un sistema de recomendación de películas. Se menciona la posibilidad de utilizar la similitud de puntuación entre películas para recomendar películas similares a los usuarios.

## Métodos utilizados
En el Proyecto Individual de MLOps, se utilizan varios métodos y enfoques para abordar diferentes aspectos del problema. Estos métodos incluyen:

Transformación de datos: Se aplican técnicas de manipulación y transformación de datos para desanidar campos anidados, rellenar valores nulos, eliminar registros inválidos y formatear fechas.

Desarrollo de API: Se utiliza el framework FastAPI para crear endpoints y exponer los datos de la empresa a través de consultas específicas, permitiendo su acceso y consumo.

Deployment: Se considera el uso de servicios como Render  para implementar y desplegar la API, asegurando su disponibilidad y accesibilidad desde la web.

Análisis exploratorio de datos (EDA): Se emplean diversas librerías de Python, como pandas profiling, missingno, sweetviz y autoviz, para realizar un análisis exploratorio de los datos, identificar relaciones entre variables, detectar outliers y patrones interesantes.

Modelo de machine learning: Se entrena un modelo de machine learning específico para el sistema de recomendación de películas, utilizando técnicas de similitud de puntuación entre películas para generar recomendaciones basadas en películas similares.

## Tecnologías
En el Proyecto Individual de MLOps, se utilizan varias tecnologías para su desarrollo. A continuación, se mencionan algunas de las tecnologías clave involucradas:

Python: El lenguaje de programación principal utilizado en todo el proyecto, tanto para el procesamiento de datos, el desarrollo de la API, el análisis exploratorio de datos y el entrenamiento del modelo de machine learning.

Pandas: Una biblioteca de Python ampliamente utilizada para la manipulación y análisis de datos, utilizada para realizar transformaciones en los datos y llevar a cabo el análisis exploratorio.

FastAPI: Un framework de desarrollo web de Python utilizado para crear la API que permite la disponibilidad y acceso a los datos y funcionalidades del sistema de recomendación.

Render: Servicios de deployment utilizados para implementar y desplegar la API, permitiendo su consumo desde la web.

Librerías de visualización de datos: Se mencionan librerías como pandas profiling, missingno, sweetviz y autoviz, que se utilizan para realizar el análisis exploratorio de los datos y generar visualizaciones informativas.

Técnicas de machine learning: Se emplean técnicas de machine learning para entrenar un modelo de recomendación de películas basado en similitudes, que ayudará a generar las recomendaciones a los usuarios. Las bibliotecas de machine learning como scikit-learn fue utilizado.

Estas son algunas de las tecnologías utilizadas en el proyecto, aunque pueden existir otras herramientas y bibliotecas adicionales según las necesidades específicas del proyecto.

## Descripción del Proyecto
El Proyecto Individual de MLOps se enfoca en desarrollar un sistema de recomendación para una startup que ofrece servicios de agregación de plataformas de streaming. El objetivo es llevar a cabo todo el ciclo de vida de un proyecto de Machine Learning, desde el tratamiento y recolección de datos hasta la implementación de un modelo funcional en producción.

El proyecto comienza con la identificación de datos de baja calidad y falta de madurez en la empresa. Se requiere realizar transformaciones en los datos, como desanidar campos anidados, rellenar valores nulos y formatear fechas. Luego, se desarrolla una API utilizando el framework FastAPI, que permite el acceso a los datos a través de consultas específicas.

Además, se propone utilizar servicios de deployment como Render para implementar la API y hacerla accesible desde la web. Paralelamente, se realiza un análisis exploratorio de los datos utilizando diferentes técnicas y librerías de visualización. Esto permite identificar relaciones entre variables, detectar outliers y patrones interesantes que pueden influir en el sistema de recomendación.

El siguiente paso es entrenar un modelo de machine learning para construir un sistema de recomendación de películas. Se utiliza la similitud de puntuación entre películas para generar recomendaciones basadas en películas similares. El modelo entrenado se implementa en la API como una función adicional.


## Empezando
Para llevar a cabo el Proyecto Individual de MLOps, se identifican varias necesidades fundamentales:

Datos de calidad: Existe la necesidad de contar con datos de calidad para desarrollar un sistema de recomendación preciso y efectivo. Esto implica la limpieza, transformación y preparación de los datos, incluyendo desanidar campos anidados, rellenar valores nulos y formatear fechas.

Herramientas de transformación de datos: Se requiere utilizar herramientas y técnicas adecuadas para realizar las transformaciones necesarias en los datos, como el uso de librerías como Pandas en Python.

Desarrollo de API: Es necesario desarrollar una API utilizando un framework como FastAPI para exponer los datos y funcionalidades del sistema de recomendación. Esto permite que los departamentos de Analytics y Machine Learning puedan acceder y consumir los datos de manera eficiente.

Deployment en servicios de hosting: Se necesita implementar la API en un servicio de deployment, como Render o Railway, para asegurar su disponibilidad y accesibilidad desde la web.

Análisis exploratorio de datos: Es esencial realizar un análisis exploratorio de los datos utilizando diversas técnicas y herramientas, como pandas profiling, missingno, sweetviz, autoviz, entre otras. Esto permite identificar relaciones entre variables, detectar outliers y patrones interesantes que pueden influir en el sistema de recomendación.

Modelo de machine learning: Se requiere entrenar un modelo de machine learning específico para el sistema de recomendación de películas. Esto implica seleccionar el algoritmo adecuado, preparar los datos de entrenamiento, evaluar el modelo y ajustarlo.

## Realizando el proyecto
El proyecto se desarrolló siguiendo un plan estructurado en varias etapas. A continuación, se presenta un resumen del proceso llevado a cabo para realizar el proyecto:

Extracción de datos: Se obtuvo el conjunto de datos necesario para el proyecto, evaluando su calidad y identificando posibles problemas.

Transformación de datos (ETL): Se realizaron las transformaciones necesarias en los datos para prepararlos para el análisis y el modelo de recomendación. Se desanidaron campos anidados, se llenaron valores faltantes, se formatearon fechas y se calcularon columnas adicionales.

Análisis exploratorio de datos (EDA): Se realizó un análisis exploratorio de los datos transformados para comprender su distribución, identificar relaciones y patrones interesantes. Se utilizaron herramientas como pandas, numpy, matplotlib y seaborn para visualizar y resumir los datos.

Desarrollo de la API: Se utilizó el framework FastAPI para crear una API que expusiera los datos de la empresa. Se implementaron funciones de endpoints para las consultas requeridas.

Deployment: Se evaluaron opciones de despliegue y se configuró la API para que fuera accesible desde la web utilizando servicios como Render.

Sistema de recomendación: Se utilizó el conjunto de datos transformados para entrenar un modelo de machine learning que proporcionara recomendaciones de películas basadas en películas similares. Se utilizaron técnicas de procesamiento de texto y cálculo de similitud para encontrar películas similares y se integró la función de recomendación en la API existente.

## Librerias utilizados
En el proyecto se utilizaron varias librerías para llevar a cabo las diferentes tareas. A continuación, se mencionan algunas de las librerías comúnmente utilizadas en cada etapa del proyecto:

En este proyecto, se nos proporcionó un archivo llamado "movies_dataset.csv" en formato CSV, el cual contenía los datos con los que íbamos a trabajar. Pandas nos permitió cargar y procesar este archivo, facilitando las tareas de transformación de datos (ETL) necesarias para su análisis y posterior uso en el proyecto.

Pandas: Para la transformación y manipulación de los datos.
NumPy: Para realizar operaciones numéricas eficientes en los datos.
Scikit-learn: Para el preprocesamiento de datos y cálculos adicionales.
Análisis exploratorio de datos (EDA):

Pandas: Para el análisis y manipulación de los datos.
Matplotlib: Para la visualización de gráficos y visualizaciones.
Seaborn: Para crear gráficos estadísticos más avanzados y estilizados.
Desarrollo de la API:

FastAPI: Un framework de desarrollo web rápido para crear la API.
Requests: Para realizar solicitudes a la API y obtener respuestas.
Sistema de recomendación:

Scikit-learn: Para construir y entrenar el modelo de recomendación.

## Deployment con RENDER : https://test-i4z7.onrender.com

Es importante tener en cuenta que esta lista de librerías es solo una muestra y pueden haberse utilizado otras librerías dependiendo de las necesidades específicas del proyecto.

## Contacto
En estas redes redes sociales comunes me encuentras:
- GitHub: github.com/jhoncuria
- LinkedIn: https://www.linkedin.com/in/edgar-jhon-curi-araujo-a1908159
- Discord: jcuri#9566
- Twitter: @JhonCuri2
- Instagram: @JhonCuri

