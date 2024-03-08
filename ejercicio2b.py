sueldo = int(input("Ingrese sueldo del comprador: "))
costo_casa = int(input("Ingrese el costo de la vivienda: "))

if sueldo <= 0:
    print("Valor incorrecto para el sueldo.")
if sueldo >=80000:
    pie = int((costo_casa*15)/100)
    resto_pago = int((costo_casa)-(pie))
    pago_mensual = int(resto_pago/120)
    print("El comprador pagará",pie,"pesos por concepto de pie de casa. El pago mensual será de",pago_mensual,"pesos.")
else:
    print("No fue posible realizar el cálculo.")
if sueldo <= 80000:
    pie = int((costo_casa*30)/100)
    resto_pago = int((costo_casa)-(pie))
    pago_mensual = int(resto_pago/84)
    print("El comprador pagará",pie,"pesos por concepto de pie de casa. El pago mensual será de",pago_mensual,"pesos.")
else:
    print("No fue posible realizar el cálculo.")