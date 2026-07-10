from src.ingesta.cargador_datos import CargadorDatos


def main():
    cargador = CargadorDatos()
    datos = cargador.descargar_datos()

    print(datos.head())


if __name__ == "__main__":
    main()