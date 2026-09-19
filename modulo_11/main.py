
import numpy as np
from perceptron_experto import perceptron, obtener_pesos, obtener_pesos_case

def encabezado(t):
    print("\n"+"="*72); print(t); print("="*72)

def caso_1():
    encabezado("CASO 1 - TALLER ANALÍTICO: DISPARO DE LA NEURONA")
    W=np.array([0.8,-0.5]); b=-10; X=np.array([50,20])
    Z=np.dot(X,W)+b
    r=perceptron(X,W,b)
    print(f"Z = (50 × 0.8) + (20 × -0.5) + (-10) = {Z}")
    print(f"Función escalón: {r} -> {'APRUEBA' if r==1 else 'RECHAZA'} el crédito")
    print("Interpretación: el peso negativo de la deuda reduce la puntuación.")

def probar(nombre, fn):
    W,b=fn(nombre)
    print(f"\nCompuerta {nombre} ({fn.__name__}): W={W}, b={b}")
    for x1 in (0,1):
        for x2 in (0,1):
            r=perceptron(np.array([x1,x2]),W,b)
            print(f"  {nombre}({x1},{x2}) = {r}")

def caso_2():
    encabezado("CASO 2 - TALLER DE LABORATORIO: COMPUERTAS")
    for nombre in ("AND","OR"):
        probar(nombre,obtener_pesos)
        probar(nombre,obtener_pesos_case)
    print("\nOR con W=[1.0,1.0], b=-0.5: funciona con una o ambas entradas activas.")

def menu():
    while True:
        encabezado("MÓDULO 11 - PERCEPTRÓN")
        print("1. Caso: disparo de la neurona")
        print("2. Caso: compuertas lógicas")
        print("0. Salir")
        opcion=input("Seleccione un caso: ").strip()
        match opcion:
            case "1": caso_1()
            case "2": caso_2()
            case "0": print("Módulo finalizado."); break
            case _: print("Opción no válida.")

if __name__=="__main__": menu()
