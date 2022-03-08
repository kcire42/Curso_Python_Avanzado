from pandas import pandas as pd


# def crear_csv(funcion):
#     def csv():
#         print("Tabla x")
#         funcion()
#         print("hola")
#     return csv()

# @crear_csv()
# def datos():
#     calificaciones = {'Mario': [10,8,8],'Maria': [10,7,9],'Pepe': [10,6,5]}
#     df = pd.Series(data = calificaciones)
#     print(df)
#     return datos

# datos()


# def decorador(func):
#     def envoltorio_func(a,b):
#         print("antes de la funcion")
#         c = func(a,b)
#         print("despues de llamar a la funcion")
#         return c
#     return envoltorio_func

# def suma(a,b):
#     print("dentro de suma")
#     return a + b

# funcion_decorada = decorador(suma)


# print(funcion_decorada(5,8))


# def funcion_decorada(func):
#     def interno(letras):
#         print("primera cosa rara")
#         funcion = func(letras)
#         print("segunda cosa rara")
#         return funcion
#     return interno

# @funcion_decorada
# def datos(letras):
#     df = pd.Series(data = letras)
#     print(df)
#     return "funciono"


# calificaciones = {'Mario': [10,8,8],'Maria': [10,7,9],'Pepe': [10,6,5]}

# datos(calificaciones)

#decorador que valida la longitud de la contraseña
def validacion(func):
    def validacion_contraseña(letras):
        if len(letras) > 6:
            print("Contraseña validada cumple la longitud")   
            func(letras)        
        else: 
            print("Contresaña validada no cumple longitud")
            quit()
        return func
    return validacion_contraseña
    
#ingrese la contraseña y valida que sean iguales
@validacion
def contraseña(letras):
    confirmacion = input("Ingrese la contraseña nuevamente: ")
    if letras == confirmacion:
        print("contraseña asegurada")
    else: 
        print("contraseña no coincide")


contraseña_nueva = input("Ingrese su contraseña: ")
contraseña(contraseña_nueva)

