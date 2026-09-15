
from experto_automatico import construir_dataset, NOMBRES_VARIABLES, CLIENTES, entrenar_arbol, extraer_reglas, predecir_cliente

def encabezado(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)

def preparar_modelo():
    X, Y = construir_dataset()
    return entrenar_arbol(X, Y, max_depth=3)

def caso_1():
    encabezado("CASO 1 - DATASET DE MARKETING")
    for i,c in enumerate(CLIENTES,1):
        estado = "HIZO CLIC" if c["hizo_clic"] else "LO IGNORÓ"
        print(f"{i:2d}. Edad={c['edad']}, Horas={c['horas_online']}, Compras={c['compras_previas']} -> {estado}")

def caso_2():
    encabezado("CASO 2 - ENTRENAMIENTO Y REGLAS APRENDIDAS")
    arbol = preparar_modelo()
    print("Árbol entrenado correctamente.")
    print("\nBASE DE REGLAS APRENDIDA:")
    print(extraer_reglas(arbol, NOMBRES_VARIABLES))

def caso_3():
    encabezado("CASO 3 - PREDICCIÓN DE CLIENTES NUEVOS")
    arbol = preparar_modelo()
    nuevos = [
        {"edad": 23, "horas_online": 6, "compras_previas": 1},
        {"edad": 58, "horas_online": 1, "compras_previas": 0},
    ]
    for c in nuevos:
        pred, prob = predecir_cliente(arbol, **c)
        print(f"{c} -> {'HARÍA CLIC' if pred else 'LO IGNORARÍA'} | confianza {prob*100:.0f}%")

def menu():
    while True:
        encabezado("MÓDULO 6 - ÁRBOL DE DECISIÓN")
        print("1. Caso: visualizar dataset")
        print("2. Caso: entrenar y mostrar reglas")
        print("3. Caso: predecir clientes nuevos")
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
