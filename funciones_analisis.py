
import pandas as pd
import matplotlib.pyplot as plt

def cargar_datos(ruta):

    df = pd.read_excel(ruta)

    return df


def calcular_promedios(df):

    resumen = df.groupby("planta")[[
        "DBO_entrada_mg_L",
        "DBO_salida_mg_L",
        "energia_aeracion_kWh",
        "lodos_generados_kg_d"
    ]].mean()

    return resumen



def grafico_dbo(resumen):

    resumen["DBO_salida_mg_L"].plot(
        kind="bar",
        figsize=(8,5)
    )

    plt.title("DBO salida promedio por planta")
    plt.ylabel("DBO mg/L")
    plt.xticks(rotation=45)

    plt.show()
