def palindromo (palabra: str):
    palabra = palabra.lower()
    palabra = palabra.replace(' ','')
    if palabra == palabra[::-1]:
        print("Es un palindromo")
    else:
        print("No es un palindromo")
    
    


if __name__ == '__main__':
    palabra : str = input()
    palindromo(palabra)