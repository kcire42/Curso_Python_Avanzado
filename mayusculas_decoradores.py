import re


def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombres):
    return f'{nombres}, recibiste el mensaje'

print(mensaje('Cesar'))
