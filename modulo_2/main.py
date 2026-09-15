
from motor_experto import (
    MotorInferencia, REGLAS_FRAUDE, construir_hechos,
    REGLAS_MOTOCICLETA, HECHOS_INICIALES_MOTOCICLETA,
)

def encabezado(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)

def caso_1():
    encabezado("CASO 1 - FRAUDE: TRANSACCIÓN SOSPECHOSA")
    motor = MotorInferencia(REGLAS_FRAUDE)
    hechos = construir_hechos(7500, "Extranjero", True, False)
    r = motor.ejecutar(hechos)
    print(r.explicar())
    print("Bloquear tarjeta:", r.hechos_finales.get("bloquear_tarjeta", False))

def caso_2():
    encabezado("CASO 2 - FRAUDE: TRANSACCIÓN NORMAL")
    motor = MotorInferencia(REGLAS_FRAUDE)
    hechos = construir_hechos(800, "Nacional", False, False)
    r = motor.ejecutar(hechos)
    print(r.explicar())
    print("Bloquear tarjeta:", r.hechos_finales.get("bloquear_tarjeta", False))

def caso_3():
    encabezado("CASO 3 - FRAUDE: TARJETA REPORTADA ROBADA")
    motor = MotorInferencia(REGLAS_FRAUDE)
    hechos = construir_hechos(100, "Nacional", False, True)
    r = motor.ejecutar(hechos)
    print(r.explicar())
    print("Memoria final:", r.hechos_finales)

def caso_4():
    encabezado("CASO 4 - MOTOCICLETA / CASCO / PERMISO")
    motor = MotorInferencia(REGLAS_MOTOCICLETA)
    r = motor.ejecutar(HECHOS_INICIALES_MOTOCICLETA)
    print(r.explicar())
    print("Memoria final:", r.hechos_finales)
    print("Resultado: permiso denegado por ser menor y requerir casco.")

def menu():
    while True:
        encabezado("MÓDULO 2 - MOTOR DE INFERENCIA")
        print("1. Caso de fraude sospechoso")
        print("2. Caso de transacción normal")
        print("3. Caso de tarjeta robada")
        print("4. Caso motocicleta / casco / permiso")
        print("0. Salir")
        opcion = input("Seleccione un caso: ").strip()
        match opcion:
            case "1": caso_1()
            case "2": caso_2()
            case "3": caso_3()
            case "4": caso_4()
            case "0":
                print("Módulo finalizado.")
                break
            case _:
                print("Opción no válida.")

if __name__ == "__main__":
    menu()
