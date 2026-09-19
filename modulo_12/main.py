
import numpy as np
from mlp_experto import (
    forward_pass, contar_parametros, interpretar_salida,
    interpretar_salida_case, describir_arquitectura_case,
)

def encabezado(t):
    print("\n"+"="*72); print(t); print("="*72)

def caso_1():
    encabezado("CASO 1 - TALLER ANALÍTICO: PARÁMETROS")
    c=contar_parametros(3,4,1)
    print("Pesos entrada->oculta:",c.pesos_entrada_oculta)
    print("Sesgos capa oculta:",c.sesgos_oculta)
    print("Pesos oculta->salida:",c.pesos_oculta_salida)
    print("Sesgo salida:",c.sesgos_salida)
    print("TOTAL:",c.total)
    print("Arquitectura:",describir_arquitectura_case(3,4,1))

def preparar():
    W1=np.array([[0.1,0.2,-0.3,0.4],[-0.5,0.6,0.7,-0.8],[0.9,-0.1,0.2,0.3]])
    b1=np.array([0.1,-0.2,0.3,-0.4])
    W2=np.array([0.5,-0.6,0.7,0.8]); b2=np.array([-0.1])
    return W1,b1,W2,b2

def caso_2():
    encabezado("CASO 2 - TALLER DE LABORATORIO: FORWARD PASS")
    W1,b1,W2,b2=preparar()
    X=np.array([0.5,0.8,0.2])
    r=forward_pass(X,W1,b1,W2,b2)
    print("Z1 =",r["Z1"]); print("A1 =",r["A1"])
    print("Predicción =",np.round(r["salida"][0],4))
    print("Interpretación módulo:",interpretar_salida(r["salida"][0]))
    print("Interpretación case:",interpretar_salida_case(r["salida"][0]))

def caso_3():
    encabezado("CASO 3 - PROCESAMIENTO BATCH DE DOS CLIENTES")
    W1,b1,W2,b2=preparar()
    X=np.array([[0.5,0.8,0.2],[0.1,0.9,0.9]])
    r=forward_pass(X,W1,b1,W2,b2)
    print("Z1:\n",r["Z1"])
    print("Predicciones:",np.round(r["salida"].flatten(),4))
    for i,p in enumerate(r["salida"].flatten(),1):
        print(f"Cliente {i} -> {interpretar_salida_case(p)}")

def menu():
    while True:
        encabezado("MÓDULO 12 - REDES NEURONALES MLP")
        print("1. Caso: conteo de parámetros")
        print("2. Caso: forward pass")
        print("3. Caso: procesamiento batch")
        print("0. Salir")
        opcion=input("Seleccione un caso: ").strip()
        match opcion:
            case "1": caso_1()
            case "2": caso_2()
            case "3": caso_3()
            case "0": print("Módulo finalizado."); break
            case _: print("Opción no válida.")

if __name__=="__main__": menu()
