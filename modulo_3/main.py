
from logica_difusa import CONJUNTOS_EXPERIENCIA, evaluar_experiencia

def encabezado(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)

def mostrar(anios):
    r = evaluar_experiencia(anios, CONJUNTOS_EXPERIENCIA)
    print(f"Experiencia: {anios} años")
    for nombre, grado in r.grados.items():
        print(f"  {nombre}: {grado*100:.0f}%")
    print(f"Categoría dominante: {r.categoria_dominante} ({r.grado_dominante*100:.0f}%)")

def caso_1(): encabezado("CASO 1 - CONDUCTOR NOVATO / TRANSICIÓN"); mostrar(3)
def caso_2(): encabezado("CASO 2 - CONDUCTOR INTERMEDIO"); mostrar(6)
def caso_3(): encabezado("CASO 3 - CONDUCTOR EXPERTO"); mostrar(12)

def menu():
    while True:
        encabezado("MÓDULO 3 - LÓGICA DIFUSA")
        print("1. Caso: 3 años de experiencia")
        print("2. Caso: 6 años de experiencia")
        print("3. Caso: 12 años de experiencia")
        print("0. Salir")
        opcion = input("Seleccione un caso: ").strip()
        match opcion:
            case "1": caso_1()
            case "2": caso_2()
            case "3": caso_3()
            case "0":
                print("Módulo finalizado.")
                break
            case _:
                print("Opción no válida.")

if __name__ == "__main__":
    menu()
