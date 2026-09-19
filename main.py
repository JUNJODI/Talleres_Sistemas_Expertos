import os
import sys
import subprocess


MODULOS = {
    "1": "Módulo 2 - Motor de Inferencia",
    "2": "Módulo 3 - Lógica Difusa",
    "3": "Módulo 5 - Defuzzificación",
    "4": "Módulo 6 - Árbol de Decisión",
    "5": "Sistema Experto IT",
    "6": "Módulo 9 - KNN",
    "7": "Módulo 10 - SVM",
    "8": "Módulo 11 - Perceptrón",
    "9": "Módulo 12 - Redes MLP",
}


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_menu():
    limpiar()

    print("=" * 60)
    print("          TRABAJO INTEGRADO - MÓDULOS CASE")
    print("=" * 60)
    print()

    for k, nombre in MODULOS.items():
        print(f"{k}. {nombre}")

    print("0. Salir")
    print()


def ejecutar_modulo(opcion):
    """
    Ejecuta el main.py correspondiente al módulo seleccionado.
    """

    rutas = {
        "1": "modulo_2",
        "2": "modulo_3",
        "3": "modulo_5",
        "4": "modulo_6",
        "5": "modulo_sistema_experto",
        "6": "modulo_9_KNN",
        "7": "modulo_10_svm",
        "8": "modulo_11",
        "9": "modulo_12",
    }

    carpeta = rutas.get(opcion)

    if carpeta is None:
        print("Opción no válida.")
        return

    archivo = os.path.join(carpeta, "main.py")

    if not os.path.exists(archivo):
        print()
        print("ERROR:")
        print(f"No se encontró el archivo:")
        print(archivo)
        print()
        input("Presiona ENTER para continuar...")
        return

    try:
        subprocess.run([sys.executable, archivo], check=True)

    except subprocess.CalledProcessError as e:
        print()
        print("=" * 60)
        print("EL MÓDULO TERMINÓ CON UN ERROR")
        print("=" * 60)
        print(f"Código de error: {e.returncode}")
        print()
        input("Presiona ENTER para volver al menú...")


def menu():

    while True:

        mostrar_menu()

        opcion = input("Seleccione un módulo: ").strip()

        if opcion == "0":
            limpiar()
            print("=" * 60)
            print("Sistema finalizado.")
            print("=" * 60)
            break

        if opcion not in MODULOS:
            print()
            print("Opción inválida.")
            input("Presiona ENTER para continuar...")
            continue

        ejecutar_modulo(opcion)

        print()
        input("Presiona ENTER para volver al menú...")


if __name__ == "__main__":
    menu()