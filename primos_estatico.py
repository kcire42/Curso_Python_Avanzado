from math import factorial


def primos(numero : int) -> bool:  
    # factorial = 1     
    # for i in range(1,numero-1):
    #     factorial *= i 
    
    # if factorial%numero == 1:
    #     print(f"Es primo")
    # else:
    #     print(f"no es primo")
    factorial = [i for i in range(1,numero) if numero % i == 0]
    
    return len(factorial) == 1

if __name__ == '__main__':
    numero : int = int(input("Ingresa un numero: "))
    if primos(numero) == True:
        print("Es un numero primo")
    else:
        print("No es un numero primo")