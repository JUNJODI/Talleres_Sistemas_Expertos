
from knn_experto import (
    distancia_euclidiana, construir_dataset, NOMBRES_VARIABLES, CLIENTES,
    entrenar_knn, predecir, votar_mayoria, votar_mayoria_binaria,
    interpretar_dimensionalidad,
)

def encabezado(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)

def caso_1():
    encabezado("CASO 1 - TALLER ANALÍTICO: VOTACIÓN ESPACIAL")
    A, B, C = (20, 30), (40, 50), (35, 45); P = (30, 40)
    d_a, d_b, d_c = distancia_euclidiana(P,A), distancia_euclidiana(P,B), distancia_euclidiana(P,C)
    print(f"d(P,A) = {d_a:.2f} -> A: NO COMPRA")
    print(f"d(P,B) = {d_b:.2f} -> B: COMPRA")
    print(f"d(P,C) = {d_c:.2f} -> C: COMPRA")
    votos=[0,1,1]
    print("\nK=1 -> C -> COMPRA")
    print(f"K=3 -> votos {votos} -> módulo: {votar_mayoria(votos)}")
    print(f"K=3 -> votos {votos} -> case:   {votar_mayoria_binaria(votos)}")
    print("¿Coinciden?:", "SÍ" if votar_mayoria(votos)==votar_mayoria_binaria(votos) else "NO")

def caso_2():
    encabezado("CASO 2 - TALLER DE LABORATORIO: CLASIFICADOR KNN")
    print(f"Dataset: {len(CLIENTES)} clientes | Variables: {NOMBRES_VARIABLES}")
    X,Y=construir_dataset(); nuevo=[33,42,2]
    for k in (1,5):
        modelo=entrenar_knn(X,Y,k=k); pred=predecir(modelo,nuevo)
        print(f"K={k}: {nuevo} -> {'COMPRA' if pred==1 else 'NO COMPRA'}")

def caso_3():
    encabezado("CASO 3 - ANÁLISIS: MALDICIÓN DE LA DIMENSIONALIDAD")
    for n in (2,3,10,50,1000): print(interpretar_dimensionalidad(n))

def menu():
    while True:
        encabezado("MÓDULO 9 - KNN")
        print("1. Caso: votación espacial")
        print("2. Caso: clasificador KNN")
        print("3. Caso: dimensionalidad")
        print("0. Salir")
        opcion=input("Seleccione un caso: ").strip()
        match opcion:
            case "1": caso_1()
            case "2": caso_2()
            case "3": caso_3()
            case "0": print("Módulo finalizado."); break
            case _: print("Opción no válida.")

if __name__=="__main__": menu()
