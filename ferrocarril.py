
DESTINO = "San Luis Potosí"
TARIFA = 900.0  
print("=== FERROCARRIL ===")
print("Destino:", DESTINO)
print("Tarifa por pasajero: $", TARIFA)


pasajeros = int(input("Ingresa el número de pasajeros: "))


total = pasajeros * TARIFA


print("\n--- RESUMEN DEL VIAJE ---")
print("Destino:", DESTINO)
print("Número de pasajeros:", pasajeros)
print("Total a pagar: $", total)
