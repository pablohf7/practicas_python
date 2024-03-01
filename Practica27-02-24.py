#PROGRAMA DE TASA DE IMPUESTO
income=float(input("Intoduce el ingreso anual: "))

if income<=85518:
    tax = income*0.18-556.02
else:
    tax = 14839.02 + (income-85518)*0.32
tax=round(tax,0) 
if tax<0:
    tax=0
    
print("El impuesto del contribuyente es igual a: ", tax)