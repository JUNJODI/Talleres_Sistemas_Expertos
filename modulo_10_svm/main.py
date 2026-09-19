
from svm_experto import (
    X_BASE,Y_BASE,agregar_punto_conflictivo,entrenar_svm,
    obtener_vectores_soporte,predecir_punto,describir_kernel,
    describir_kernel_case,recomendar_kernel_case,
)

def encabezado(t):
    print("\n"+"="*72); print(t); print("="*72)

def caso_1():
    encabezado("CASO 1 - KERNEL LINEAL")
    modelo=entrenar_svm(X_BASE,Y_BASE,kernel="linear")
    print("Vectores de soporte:"); print(obtener_vectores_soporte(modelo))
    print("Descripción módulo:",describir_kernel("linear"))
    print("Descripción case:",describir_kernel_case("linear"))
    print("Predicción [5,4]: Clase",predecir_punto(modelo,[5,4]))

def caso_2():
    encabezado("CASO 2 - PUNTO CONFLICTIVO Y REENTRENAMIENTO")
    X,Y=agregar_punto_conflictivo(X_BASE,Y_BASE)
    print("Dataset con [5,5] como Clase A (0):"); print(X)
    modelo=entrenar_svm(X,Y,kernel="linear")
    aciertos=sum(modelo.predict(X)==Y)
    print(f"Kernel lineal: {aciertos}/{len(Y)} puntos correctamente clasificados.")

def caso_3():
    encabezado("CASO 3 - KERNEL RBF")
    X,Y=agregar_punto_conflictivo(X_BASE,Y_BASE)
    modelo=entrenar_svm(X,Y,kernel="rbf")
    aciertos=sum(modelo.predict(X)==Y)
    print(f"Kernel RBF: {aciertos}/{len(Y)} puntos correctamente clasificados.")
    print("Descripción módulo:",describir_kernel("rbf"))
    print("Descripción case:",describir_kernel_case("rbf"))
    print("Predicción [5,4]: Clase",predecir_punto(modelo,[5,4]))

def caso_4():
    encabezado("CASO 4 - REFLEXIÓN Y SELECCIÓN DE KERNEL")
    escenarios=[
        "Un sistema de reconocimiento facial que debe distinguir rostros",
        "Detección de un tumor rodeado completamente por tejido sano",
        "Clasificar correos como spam vs no-spam con palabras claramente separables",
    ]
    for e in escenarios: print(f"\n{e}\n -> {recomendar_kernel_case(e)}")

def menu():
    while True:
        encabezado("MÓDULO 10 - SVM")
        print("1. Caso: kernel lineal")
        print("2. Caso: punto conflictivo")
        print("3. Caso: kernel RBF")
        print("4. Caso: reflexión")
        print("0. Salir")
        opcion=input("Seleccione un caso: ").strip()
        match opcion:
            case "1": caso_1()
            case "2": caso_2()
            case "3": caso_3()
            case "4": caso_4()
            case "0": print("Módulo finalizado."); break
            case _: print("Opción no válida.")

if __name__=="__main__": menu()
