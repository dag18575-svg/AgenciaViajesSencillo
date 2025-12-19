def mostrar_menu():
    print("\n=== Agencia de Viajes AeroPlus ===")
    print("1. Ver vuelos disponibles")
    print("2. Reservar un vuelo")
    print("3. Salir")

def mostrar_vuelos():
    print("\nVuelos disponibles:")
    print("1. Ciudad de México → Cancún - $3200 MXN")
    print("2. Guadalajara → Nueva York - $8500 MXN")
    print("3. Monterrey → Madrid - $14500 MXN")

def reservar_vuelo():
    nombre = input("\nIngresa tu nombre: ")
    mostrar_vuelos()
    opcion = input("Elige el número del vuelo: ")

    if opcion == "1":
        vuelo = "CDMX → Cancún"
    elif opcion == "2":
        vuelo = "Guadalajara → Nueva York"
    elif opcion == "3":
        vuelo = "Monterrey → Madrid"
    else:
        print("Opción no válida")
        return

    print("\n✅ Reserva exitosa")
    print(f"Cliente: {nombre}")
    print(f"Vuelo seleccionado: {vuelo}")


while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        mostrar_vuelos()
    elif opcion == "2":
        reservar_vuelo()
    elif opcion == "3":
        print("Gracias por volar con AeroPlus ✈️")
        break
    else:
        print("Opción inválida, intenta de nuevo.")
#cervantes