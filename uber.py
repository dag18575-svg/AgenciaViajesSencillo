destino = "Centro de la ciudad"
tarifa_base = 50        
costo_por_pasajero = 20 

print("Destino:", destino)
pasajeros = int(input("Ingresa el número de pasajeros: "))

total_pagar = tarifa_base + (pasajeros * costo_por_pasajero)

print("\n--- RESUMEN DEL VIAJE ---")
print("Destino:", destino)
print("Pasajeros:", pasajeros)
print("Tarifa base: $", tarifa_base)
print("Costo por pasajero: $", costo_por_pasajero)
print("Total a pagar: $", total_pagar)
