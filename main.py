from src.ingesta.cargador_datos import CargadorDatos
from src.gestor.gestor_partidos import GestorPartidos


def main():

    cargador = CargadorDatos()
    datos = cargador.descargar_datos()
    datos_mundial = cargador.guardar_partidos_mundial(datos)

    gestor = GestorPartidos(datos_mundial)

    print("Cantidad total de partidos:")
    print(gestor.total_partidos())

    print("\nColumnas disponibles:")
    print(gestor.listar_columnas())
    print("\nTorneos disponibles:")
    print(gestor.listar_torneos())
    mundial = gestor.filtrar_mundial()

    print("\nCantidad de partidos del Mundial:")
    print(len(mundial))

    print("\nPrimeros partidos del Mundial:")
    print(mundial.head())
    print("\nPartidos de Brasil:")

    brasil = gestor.get_por_equipo("Brazil")

    print(brasil[["date", "home_team", "away_team", "home_score", "away_score"]].head())

    print(f"\nBrasil ha jugado {len(brasil)} partidos en la Copa del Mundo.")
    print("\nPartidos del Mundial de 2022:")

    mundial_2022 = gestor.get_por_anio(2022)

    print(mundial_2022[["date", "home_team", "away_team"]].head())

    print(f"\nEn 2022 se jugaron {len(mundial_2022)} partidos.")
    print("\nPartidos jugados en Qatar:")

    qatar = gestor.get_por_sede("Qatar")

    print(qatar[["date", "home_team", "away_team"]].head())

    print(f"\nEn Qatar se jugaron {len(qatar)} partidos del Mundial.")
    print("\nCantidad de partidos según condición de sede:")

    print(gestor.ventaja_local())


if __name__ == "__main__":
    main()