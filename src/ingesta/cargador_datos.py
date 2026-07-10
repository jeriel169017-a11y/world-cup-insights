import pandas as pd


class CargadorDatos:

    URL_CSV = "https://raw.githubusercontent.com/martj42/international_results/master/results.csv"

    def __init__(self):
        self.datos = None

    def descargar_datos(self):
        """Descarga el archivo CSV desde GitHub."""
        self.datos = pd.read_csv(self.URL_CSV)
        return self.datos