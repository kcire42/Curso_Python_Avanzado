import time

# def FiboIter():

#     def __init__(self,max_number:int):
#         self.max_number = max_number

#     def __iter__(self):
#         self.n1 = 0
#         self.n2 = 1
#         self.counter = 0
#         return self

#     def __next__(self):
#         if self.counter == 0:
#             self.counter += 1
#             return self.n1
#         elif self.counter == 1:
#             self.counter += 1
#             return self.n2
#         else:
#             self.aux = self.n1 + self.n2
#             # self.n1 = self.n2
#             # self.n2 = self.aux
#             self.n1 , self.n2 = self.n2 , self.aux
#             self.counter += 1
#             if self.aux > self.max_number:
#                 raise StopIteration 
#             return self.aux

def fibonacci(max:int):
    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == 0 :
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else: 
            aux = n1 + n2 
            n1 , n2 = n2 , aux
            counter += 1
            if aux > max:
                raise StopIteration
            yield aux


if __name__ == "__main__":
    while True:
        try:
            numero_maximo = int(input("Ingrese el numeor maximo: "))
            fibo = fibonacci(numero_maximo)
            for element in fibo:
                print(element) 
                time.sleep(0.05)
        except ValueError:
            print("solo numeros")

