import matplotlib.pyplot as plt


class Visualizador:

    def __init__(self, datos):
        self.datos = datos

    def grafico_top_equipos(self):
        """
        Grafica las 10 selecciones con más partidos jugados.
        """

        equipos = (
            self.datos["home_team"]
            .value_counts()
            .add(self.datos["away_team"].value_counts(), fill_value=0)
            .sort_values(ascending=False)
            .head(10)
        )

        print(equipos)

        plt.figure(figsize=(10, 6))

        equipos.plot(kind="bar")

        plt.title("Top 10 selecciones con más partidos")

        plt.xlabel("Selección")

        plt.ylabel("Cantidad de partidos")

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.show()