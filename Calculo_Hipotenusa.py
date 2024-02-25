print("CALCULO DE LA HIPOTENUSA")
print("------------------------")
n_cal=int(input("Ingrese el numero de calculo de hipotenusa: "))

for i in range(n_cal):
   a=float(input("Ingrese el cateto \"a\": "))
   b=float(input("Ingrese el cateto \"b\": "))
   c=(a**2+b**2)**0.5
   print("c =", c) 
print("---------------")
print("FIN DE PROGRAMA") 
input() 