import os
import pandas as pd


class CargadorDatos:

    URL_CSV = "https://raw.githubusercontent.com/martj42/international_results/master/results.csv"

    def __init__(self):
        self.datos = None

    def descargar_datos(self):
        """Descarga el archivo CSV desde GitHub."""
        self.datos = pd.read_csv(self.URL_CSV)
        return self.datos

    def guardar_partidos_mundial(self, datos):
        """
        Filtra únicamente los partidos del Mundial y los guarda
        en data/raw/partidos-mundial.csv
        """

        mundial = datos[datos["tournament"] == "FIFA World Cup"]

        os.makedirs("data/raw", exist_ok=True)

        ruta = "data/raw/partidos-mundial.csv"

        mundial.to_csv(ruta, index=False, encoding="utf-8")

        print(f"\nArchivo guardado correctamente en: {ruta}")

        return mundial