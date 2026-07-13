class Utilidades:
    """
    Clase con funciones auxiliares reutilizables.
    """

    @staticmethod
    def obtener_anio(fecha):
        """
        Extrae el año de una fecha en formato YYYY-MM-DD.
        """
        return str(fecha)[:4]

    @staticmethod
    def formatear_numero(numero):
        """
        Devuelve un número con separador de miles.
        """
        return f"{numero:,}"

    @staticmethod
    def imprimir_titulo(texto):
        """
        Imprime un título con una línea decorativa.
        """
        print("\n" + "=" * 50)
        print(texto)
        print("=" * 50)