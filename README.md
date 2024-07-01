# Análisis exploratorio de los salarios de la Universidad Autónoma de Nuevo León

## Descripción
Este proyecto realiza un análisis exploratorio de los datos de salarios de la Universidad Autónoma de Nuevo León (UANL). El objetivo es entender la distribución de los sueldos, las diferencias entre dependencias y tupos de empleados, entre otras características relevantes.

## Estructura del proyecto
```
uanl-payroll-analysis/
├── Practicas/
│   └── Practica1/
│       ├── img/
│       │   ├── boxplot_sueldos/
│       │   ├── violinplot_sueldos/
│       │   ├── grafico_pastel_dependencias.png
│       │   ├── grafico_barras_tipos_empleo.png
│       │   └── histograma_sueldos.png
│       ├── processed_uanl_pagos.csv
│       ├── sueldos_dependencia.csv
│       ├── sueldos_fecha.csv
│       └── uanl_payroll_analysis.ipynb
├── Reportes/
│   └── Practica1.pdf
├── .gitignore
├── LICENSE
└── README.md
```

## Archivos principales
- `uanl_payroll_analysis.ipynb`: Libreta de Jupyter que contiene el análisis exploratorio completo.
- `processed_uanl_pagos.csv`: Datos procesados resultantes.
- `sueldos_dependencia.csv`: Estadísticas descriptivas de sueldos por dependencia.
- `sueldos_fecha.csv`: Estadísticas descriptivas de sueldos por fecha.
- `img/`: Carpeta que contiene las imágenes generadas durante el análisis, incluyendo gráficas de distribución, de pastel, de barras, etc.
- `Reportes/Practica1.pdf`: Reporte en PDF de la práctica.

## Requisitos
Para ejecutar el análisis, es necesario tener instaladas las siguientes bibliotecas de Python:
- pandas
- matplotlib
- seaborn
- scipy
- statsmodels

Se pueden instalar estas dependencias utilizando `pip`:
```sh
pip install pandas matplotlib seaborn scipy statsmodels
```

## Ejecución
1. Clonar el repositorio
```sh
git clone https://github.com/SAElizondoR/uanl-payroll-analysis.git
cd uanl-payroll-analysis
```

2. Navegar a la carpeta de la práctica 1:
```sh
cd Practicas/Practica1
```

3. Ejecutar la libreta de Jupyter:
```sh
jupyter notebook uanl_payroll_analysis.ipynb
```

## Resultados
El análisis exploratorio incluye lo siguiente:
* Descripción general del conjunto de datos.
* Estadísticas descriptivas de los sueldos netos.
* Estadísticas descriptivas por dependencia.
* Estadísticas descriptivas por fecha.
* Gráficas de distribución.
* Pruebas de hipótesis para diferencias de sueldos entre dependencias.
