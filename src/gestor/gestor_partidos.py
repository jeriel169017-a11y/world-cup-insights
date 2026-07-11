import pandas as pd


class GestorPartidos:

    def __init__(self, datos: pd.DataFrame):
        self.datos = datos

    def total_partidos(self):
        """Retorna la cantidad total de partidos."""
        return len(self.datos)

    def listar_columnas(self):
        """Retorna las columnas del DataFrame."""
        return list(self.datos.columns)
    def listar_torneos(self):
        """Retorna la lista de torneos disponibles."""
        return sorted(self.datos["tournament"].unique())

    def filtrar_mundial(self):
        """Retorna únicamente los partidos de la Copa del Mundo."""
        return self.datos[self.datos["tournament"] == "FIFA World Cup"]

    def get_por_equipo(self, equipo):
        """
        Retorna todos los partidos donde participó un equipo.
        """
        return self.datos[
            (self.datos["home_team"] == equipo) |
            (self.datos["away_team"] == equipo)
            ]

    def get_por_anio(self, anio):
        """
        Retorna todos los partidos de un año específico.
        """
        return self.datos[
            self.datos["date"].str.startswith(str(anio))
        ]

    def get_por_sede(self, pais):
        """
        Retorna todos los partidos jugados en un país específico.
        """
        return self.datos[
            self.datos["country"] == pais
            ]

    def ventaja_local(self):
        """
        Retorna la cantidad de partidos en sede neutral y no neutral.
        """
        return self.datos["neutral"].value_counts()