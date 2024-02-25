#Ecabezado del programa
print("Cálculo del TMBF de dos equipos")
horas_operativas=float(input("Ingrese el numero de horas operativas de las maquinas: "))

print("Ingreso de datos del primer equipo: ")
horas1=float(input("Ingrese la horas que estuvo parado el equipo: "))
fallas1=float(input("Ingrese el numero de paradas: "))
MTBF1=(horas_operativas-horas1)/fallas1

print("Ingreso de datos del segundo equipo: ")
horas2=float(input("Ingrese la horas que estuvo parado el equipo: "))
fallas2=float(input("Ingrese el numero de paradas: "))
MTBF2=(horas_operativas-horas2)/fallas2

if MTBF1>MTBF2:
    print(f"El MTBF de la maquina 1 es: {MTBF1} y el MTBF de la maquina 2 es: {MTBF2}")
    print("Al obtener la maquina 1 un mayor valor, hace mas fiable el funcionamiento de la maquina")
elif MTBF1==MTBF2:
    print(f"El MTBF de la maquina 1:{MTBF1} y el MTBF de la maquina 2:{MTBF2}")
    print("Al obtener las maquinas el mismo valor, se debera calcular la desvicación estandar de los datos")
else:
    print(f"Al MTBF de la maquina 1:{MTBF1} y el MTBF de la maquina 2:{MTBF2}")
    print("Al obtener la maquina 2 un mayor valor, hace mas fiable la maquina")


