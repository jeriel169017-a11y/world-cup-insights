from src.ingesta.cargador_datos import CargadorDatos
from src.gestor.gestor_partidos import GestorPartidos
from src.eda.procesador_eda import ProcesadorEDA
from src.visualizacion.visualizador import Visualizador


def main():
    print("ENTRÉ AL MAIN")

        # Cargar datos
    cargador = CargadorDatos()
    datos = cargador.descargar_datos()
    datos_mundial = cargador.guardar_partidos_mundial(datos)

    # Crear objetos
    gestor = GestorPartidos(datos_mundial)

    eda = ProcesadorEDA(datos_mundial)
    eda.limpiar_datos()

    visualizador = Visualizador(datos_mundial)

    # Información general
    print("Cantidad total de partidos:")
    print(gestor.total_partidos())

    print("\nColumnas disponibles:")
    print(gestor.listar_columnas())

    print("\nTorneos disponibles:")
    print(gestor.listar_torneos())

    # Mundial
    mundial = gestor.filtrar_mundial()

    print("\nCantidad de partidos del Mundial:")
    print(len(mundial))

    print("\nPrimeros partidos del Mundial:")
    print(mundial.head())

    # Brasil
    brasil = gestor.get_por_equipo("Brazil")

    print("\nPartidos de Brasil:")
    print(brasil[["date", "home_team", "away_team", "home_score", "away_score"]].head())

    print(f"\nBrasil ha jugado {len(brasil)} partidos en la Copa del Mundo.")

    # Mundial 2022
    mundial_2022 = gestor.get_por_anio(2022)

    print("\nPartidos del Mundial de 2022:")
    print(mundial_2022[["date", "home_team", "away_team"]].head())

    print(f"\nEn 2022 se jugaron {len(mundial_2022)} partidos.")

    # Qatar
    qatar = gestor.get_por_sede("Qatar")

    print("\nPartidos jugados en Qatar:")
    print(qatar[["date", "home_team", "away_team"]].head())

    print(f"\nEn Qatar se jugaron {len(qatar)} partidos del Mundial.")

    # Condición de sede
    print("\nCantidad de partidos según condición de sede:")
    print(gestor.ventaja_local())

    # EDA
    print("\nDatos faltantes:")
    print(eda.datos_faltantes())

    print("\nPartidos con datos faltantes:")
    print(eda.mostrar_datos_faltantes())

    print("\nResumen estadístico:")
    print(eda.resumen_descriptivo())

    eda.agregar_total_goles()

    print("\nPrimeros partidos con total de goles:")
    print(
        eda.datos[
            [
                "home_team",
                "away_team",
                "home_score",
                "away_score",
                "total_goles"
            ]
        ].head()
    )

    # Gráfico
    print("\nMostrando gráfico...")
    visualizador.grafico_top_equipos()


if __name__ == "__main__":
    main()