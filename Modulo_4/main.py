
from defuzzificacion import validar_contra_taller_analitico, X_TALLER, MU_TALLER, calcular_fuerza_frenado

def encabezado(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)

def caso_1():
    encabezado("CASO 1 - VALIDACIÓN DEL CENTRO DE GRAVEDAD")
    coincide, resultado = validar_contra_taller_analitico()
    numerador = sum(x*m for x,m in zip(X_TALLER, MU_TALLER))
    denominador = sum(MU_TALLER)
    print("X =", X_TALLER.tolist())
    print("μ =", MU_TALLER.tolist())
    print(f"Numerador: {numerador}")
    print(f"Denominador: {denominador}")
    print(f"COG calculado: {resultado:.4f}")
    print("COG esperado: 23.3333")
    print("Coincide:", "SÍ" if coincide else "NO")

def caso_2():
    encabezado("CASO 2 - FRENADO AUTOMÁTICO")
    x, curva, fuerza = calcular_fuerza_frenado(70.0, 10.0, 100)
    print(f"Puntos: {len(x)}")
    print(f"Rango: {x[0]:.0f} a {x[-1]:.0f} N")
    print("Curva: Gaussiana, centro=70 N, sigma=10")
    print(f"Fuerza Crisp: {fuerza:.4f} N")

def menu():
    while True:
        encabezado("MÓDULO 5 - DEFUZZIFICACIÓN")
        print("1. Caso: validación COG")
        print("2. Caso: sistema de frenado automático")
        print("0. Salir")
        opcion = input("Seleccione un caso: ").strip()
        match opcion:
            case "1": caso_1()
            case "2": caso_2()
            case "0":
                print("Módulo finalizado.")
                break
            case _:
                print("Opción no válida.")

if __name__ == "__main__":
    menu()
