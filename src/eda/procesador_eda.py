import pandas as pd


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