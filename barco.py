def mostrar_menu():
    print("\n=== Agencia de Viajes MarAzul ===")
    print("1. Ver viajes disponibles")
    print("2. Reservar un viaje")
    print("3. Salir")

def mostrar_viajes():
    print("\nViajes en barco disponibles:")
    print("1. Isla Paraíso - 3 días - $2500 MXN")
    print("2. Puerto Aventura - 5 días - $4000 MXN")
    print("3. Crucero Familiar - 7 días - $6500 MXN")

def reservar_viaje():
    nombre = input("\nIngresa tu nombre: ")
    mostrar_viajes()
    opcion = input("Elige el número del viaje: ")

    if opcion == "1":
        viaje = "Isla Paraíso"
    elif opcion == "2":
        viaje = "Puerto Aventura"
    elif opcion == "3":
        viaje = "Crucero Familiar"
    else:
        print("Opción no válida")
        return

    print(f"\n✅ Reserva exitosa")
    print(f"Cliente: {nombre}")
    print(f"Viaje seleccionado: {viaje}")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        mostrar_viajes()
    elif opcion == "2":
        reservar_viaje()
    elif opcion == "3":
        print("Gracias por viajar con MarAzul 🌊")
        break
    else:
        print("Opción inválida, intenta de nuevo.")
