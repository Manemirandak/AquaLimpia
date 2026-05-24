
# Proyecto de Analisis de Datos
## AquaLimpia S.A.

---

# Descripcion del Proyecto

Este proyecto tiene como objetivo analizar el desempeño operacional y ambiental de las plantas de tratamiento de aguas residuales de AquaLimpia S.A., utilizando herramientas de ciencia de datos y visualizacion en Python.

El analisis busca identificar patrones asociados a incumplimientos normativos en los niveles de DBO, evaluar diferencias entre plantas y apoyar la toma de decisiones mediante dashboards y reportes automatizados.

---

# Objetivos del Proyecto

## Objetivo General

Analizar el comportamiento de las plantas de tratamiento de AquaLimpia S.A. para detectar patrones relevantes y apoyar la toma de decisiones operacionales y ambientales.

## Objetivos Especificos

- Analizar los niveles de DBO de entrada y salida.
- Comparar el desempeño de las distintas plantas.
- Evaluar el consumo energetico y generacion de lodos.
- Detectar posibles incumplimientos normativos.
- Construir dashboards exploratorios.
- Generar reportes para distintas areas de la empresa.

---

# Dataset Utilizado

Archivo:
`dataset_set_A_aguas_residuales.xlsx`

Variables principales:

- fecha_registro
- planta
- caudal_entrada_m3_d
- DBO_entrada_mg_L
- SST_entrada_mg_L
- pH_entrada
- energia_aeracion_kWh
- lodos_generados_kg_d
- DBO_salida_mg_L
- cumplimiento_norma

---

# Herramientas Utilizadas

- Python
- Pandas
- Matplotlib
- Google Colab
- GitHub

---

# Proceso Analitico

## 1. Carga de Datos

Se importo el dataset utilizando Pandas mediante la funcion:

```python
df = pd.read_excel("/content/dataset_set_A_aguas_residuales (1).xlsx")
```

## 2. Exploracion Inicial

Se revisaron:
- tipos de datos
- valores nulos
- estructura de columnas
- registros disponibles

## 3. Limpieza y Preparacion

Se verifico la calidad de los datos para evitar errores en el analisis.

## 4. Analisis Exploratorio

Se calcularon metricas promedio por planta utilizando `groupby()` para analizar:

- DBO salida
- consumo energetico
- generacion de lodos
- cumplimiento normativo

## 5. Visualizacion de Datos

Se construyo un dashboard exploratorio utilizando Matplotlib para representar graficamente:

- DBO promedio por planta
- consumo energetico promedio
- cumplimiento normativo

## 6. Generacion de Reportes

Se exportaron reportes diferenciados para:

- Area Operaciones
- Area Gestion Ambiental

---

# Resultados Principales

El analisis permitio identificar diferencias operacionales entre plantas de tratamiento, observando variaciones en los niveles de DBO de salida y en el consumo energetico. Ademas, el dashboard exploratorio facilito la deteccion visual de posibles focos de incumplimiento normativo y entrego informacion relevante para apoyar la toma de decisiones.

---

# Estructura del Proyecto

```text
AquaLimpia/
│
├── datos/
├── notebooks/
├── scripts/
├── reportes/
├── graficos/
└── README.md
```

---

# Repositorio GitHub

El proyecto se almacena en GitHub para facilitar:

- control de versiones
- trabajo colaborativo
- trazabilidad
- respaldo del proyecto

---

# Conclusiones

La utilizacion de herramientas de ciencia de datos permitio analizar el comportamiento de las plantas de tratamiento de AquaLimpia S.A. mediante un flujo reproducible y organizado. La documentacion tecnica favorece la comprension del proyecto, facilita la reutilizacion del analisis y fortalece la colaboracion entre las distintas areas involucradas.


