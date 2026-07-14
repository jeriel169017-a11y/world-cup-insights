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

    def equipo_con_mas_victorias(self):
        """
        Retorna las selecciones con más victorias en la Copa del Mundo.
        """

        victorias = {}

        for _, partido in self.datos.iterrows():

            if partido["home_score"] > partido["away_score"]:
                ganador = partido["home_team"]

            elif partido["away_score"] > partido["home_score"]:
                ganador = partido["away_team"]

            else:
                continue

            victorias[ganador] = victorias.get(ganador, 0) + 1

        return (
            sorted(victorias.items(), key=lambda x: x[1], reverse=True)
        )

    def promedio_goles_por_partido(self):
        """
        Calcula el promedio de goles por partido.
        """

        total_goles = (
                self.datos["home_score"] +
                self.datos["away_score"]
        )

        return total_goles.mean()

    def pais_con_mas_partidos(self):
        """
        Retorna los países sede con más partidos jugados.
        """

        return self.datos["country"].value_counts()

    def partido_con_mas_goles(self):
        """
        Retorna el partido con mayor cantidad de goles.
        """

        datos = self.datos.copy()

        datos["total_goles"] = (
                datos["home_score"] +
                datos["away_score"]
        )

        return datos.sort_values(
            by="total_goles",
            ascending=False
        ).head(1)

    def listar_equipos(self):
        """
        Retorna todas las selecciones disponibles.
        """

        equipos = sorted(
            set(
                self.datos["home_team"].dropna().astype(str)
            ).union(
                set(
                    self.datos["away_team"].dropna().astype(str)
                )
            )
        )

        return equipos