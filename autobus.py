def mostrar_menu():
    print("\n=== Autobuses AeroPlus ===")
    print("Destino único: Ciudad Central")
    print("1. Ver información del viaje")
    print("2. Reservar viaje")
    print("3. Salir")

def mostrar_info():
    print("\nInformación del viaje:")
    print("Destino: Ciudad Central")
    print("Tarifa por pasajero: $250 MXN")

def reservar_viaje():
    nombre = input("\nIngresa tu nombre: ")
    pasajeros = int(input("Ingresa el número de pasajeros: "))

    tarifa = 250
    total_pagar = pasajeros * tarifa

    print("\n✅ Reserva exitosa")
    print("Cliente:", nombre)
    print("Destino: Ciudad Central")
    print("Pasajeros:", pasajeros)
    print("Total a pagar: $", total_pagar, "MXN")


while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        mostrar_info()
    elif opcion == "2":
        reservar_viaje()
    elif opcion == "3":
        print("Gracias por viajar con Autobuses AeroPlus 🚌")
        break
    else:
        print("Opción inválida, intenta de nuevo.")
