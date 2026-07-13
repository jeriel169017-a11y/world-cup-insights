import pandas as pd
from pathlib import Path


class ProcesadorEDA:

    def __init__(self, datos: pd.DataFrame):
        self.datos = datos

    def datos_faltantes(self):
        """
        Retorna la cantidad de valores nulos por columna.
        """
        return self.datos.isnull().sum()

    def mostrar_datos_faltantes(self):
        """
        Muestra las filas que contienen valores nulos.
        """
        return self.datos[self.datos.isnull().any(axis=1)]

    def resumen_descriptivo(self):
        """
        Retorna estadísticas descriptivas.
        """
        return self.datos.describe()

    def agregar_total_goles(self):
        """
        Crea una columna con el total de goles por partido.
        """
        self.datos["total_goles"] = (
                self.datos["home_score"] +
                self.datos["away_score"]
        )

        return self.datos




    def limpiar_datos(self):
        """
        Elimina los registros con valores nulos.
        """
        self.datos = self.datos.dropna()

        return self.datos

    from pathlib import Path

    def guardar_datos_procesados(self):
        """
        Guarda los datos procesados en la carpeta data/processed.
        """

        ruta = Path("data/processed/partidos_procesados.csv")

        print("Guardando en:", ruta.resolve())

        self.datos.to_csv(
            ruta,
            index=False,
            encoding="utf-8"
        )

        print(f"Archivo procesado guardado en: {ruta}")
        """
        Guarda los datos procesados en la carpeta data/processed.
        """
        ruta = "data/processed/partidos_procesados.csv"

        self.datos.to_csv(
            ruta,
            index=False,
            encoding="utf-8"
        )

        print(f"\nArchivo procesado guardado en: {ruta}")