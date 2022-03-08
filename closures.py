# def make_multiplier(x):
#     print(x)
#     def multiplier(n):
#         print(n)
#         print(x)
#         return x*n
#     return multiplier

#times10 = make_multiplier(10)
#times4 = make_multiplier(4)


#print(times10(3))
# print(times4(5))
# print(times10(times4(2)))

# def funcion_principal():
#     a = 'a'
#     b = 'b'
#     def funcion_anidada():
#         c = 'c'
#         nonlocal b
#         print(a)
#         print(b)
#         b = 'cambie b'

#     funcion_anidada()
#     print(b)

# funcion_principal()




# def saludar_usuario(username):
#     mensaje = 'Hola' + username
#     def saludar():
#         print(mensaje)
#     return saludar

#Hola 3 -> HolaHolaHola
#Facundo 2 -> FacundoFacundo
#Platzi -> PlatziPlatziPlatziPlatzi

# def make_repeater(n):
#     def str_repeater(string):
#         assert type(string) == str, "Solo se pueden colocar strings"
#         return string*n
    
#     return str_repeater




def make_division(divider : float):
    def division(dividend: float) -> float:
        assert divider != 0, "No se puede dividir entre 0"
        return dividend/divider
    return division




if __name__ == '__main__':
    divider = float(input("Ingrese un divisor: "))
    dividend = float(input("Ingrese un dividento: "))
    division = make_division(divider)
    print(division(dividend))
    
