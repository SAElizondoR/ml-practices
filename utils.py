import pandas as pd
from scipy.io import arff

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def procesar_datos_entrada(ruta):
    # Leer el archivo ARFF
    datos = pd.DataFrame(arff.loadarff(ruta)[0])

    # Convertir formato de columnas objeto a cadena de caracteres
    for col in datos.columns:
        datos[col] = datos[col].apply(
            lambda x: x.decode('utf-8') if isinstance(x, bytes) else x
        )
    # Sustituir nombres de clases por valores numéricos
    if 'class' in datos.columns:
        datos['class'] = datos['class'].map({'normal': 0, 'anomaly': 1})
    # Identificar y convertir columnas categóricas
    columnas_categoricas = datos.select_dtypes(include=['object']).columns
    datos[columnas_categoricas] \
        = datos[columnas_categoricas].astype('category')

    return datos.drop('class', axis=1), datos['class']

def obtener_preprocesador(X):
    # Definir columnas categóricas y numéricas
    X_categoricas = X.select_dtypes(include=['category']).columns
    X_numericas = X.columns.difference(X_categoricas)

    # Preprocesamiento
    return ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), X_numericas),
            ('cat', OneHotEncoder(handle_unknown='ignore'), X_categoricas)
        ]
    )
