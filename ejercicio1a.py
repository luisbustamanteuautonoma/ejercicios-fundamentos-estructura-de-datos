precio = int(input("¿Cuál es el valor general de la entrada?: "))
edad = int(input("Ingrese edad del asistente: "))
if edad < 5:
    print("No pueden ingresar menores de 5 años al teatro.")
if edad >= 5 and edad <= 14:
    dinero_no_percibido = int((precio*35)/100)
    preciof = int((precio)-(dinero_no_percibido))
    print("El dinero no percibido con la entrada vendida es de",dinero_no_percibido,"pesos. La entrada tiene un valor final de",preciof,"pesos")
if edad >=15 and edad <= 19:
    dinero_no_percibido = int((precio*25)/100)
    preciof = int((precio)-(dinero_no_percibido))
    print("El dinero no percibido con la entrada vendida es de",dinero_no_percibido,"pesos. La entrada tiene un valor final de",preciof,"pesos")
if edad >=20 and edad <=45:
    dinero_no_percibido = int((precio*10)/100)
    preciof = int((precio)-(dinero_no_percibido))
    print("El dinero no percibido con la entrada vendida es de",dinero_no_percibido,"pesos. La entrada tiene un valor final de",preciof,"pesos")
if edad >=46 and edad <=65:
    dinero_no_percibido = int((precio*25)/100)
    preciof = int((precio)-(dinero_no_percibido))
    print("El dinero no percibido con la entrada vendida es de",dinero_no_percibido,"pesos. La entrada tiene un valor final de",preciof,"pesos")
if edad >= 66:
    dinero_no_percibido = int((precio*35)/100)
    preciof = int((precio)-(dinero_no_percibido))
    print("El dinero no percibido con la entrada vendida es de",dinero_no_percibido,"pesos. La entrada tiene un valor final de",preciof,"pesos")