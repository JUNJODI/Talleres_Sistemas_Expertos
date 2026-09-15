
from sistema_experto import ServidorEstado, diagnosticar_servidor

def encabezado(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)

def ejecutar(caso):
    d = diagnosticar_servidor(caso)
    print("Datos:", caso.to_dict())
    print("Veredicto:", d)
    print("\nExplicación:")
    print(d.explicar())

def construir_caso(numero):
    casos = {
        1: ServidorEstado(45,35,120,65,True),
        2: ServidorEstado(55,40,90,85,False),
        3: ServidorEstado(50,45,100,88,True),
        4: ServidorEstado(95,8,150,70,True),
        5: ServidorEstado(80,30,250,60,True),
        6: ServidorEstado(40,50,600,55,True),
        7: ServidorEstado(82,40,100,60,True),
    }
    return casos[numero]

def menu():
    while True:
        encabezado("SISTEMA EXPERTO IT - MENÚ DE CASOS")
        print("1. Caso normal")
        print("2. Sobrecalentamiento + ventilador apagado")
        print("3. Sobrecalentamiento + ventilador activo")
        print("4. Saturación de recursos")
        print("5. Recursos elevados + latencia")
        print("6. Latencia crítica")
        print("7. CPU elevada")
        print("0. Salir")
        opcion = input("Seleccione un caso: ").strip()
        match opcion:
            case "1" | "2" | "3" | "4" | "5" | "6" | "7":
                ejecutar(construir_caso(int(opcion)))
            case "0":
                print("Sistema finalizado.")
                break
            case _:
                print("Opción no válida.")

if __name__ == "__main__":
    menu()
