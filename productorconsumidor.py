import threading
import time
import random

#Creamos una lsita para simular el buffer
buffer = []
#Establecemos la cantidad de elementos que puede tener el buffer, numero de elemento suq elo sproductores puedes oclocar en el buffer antes de que los consumidores puedan procesarlos.
capacidad_buffer = 10

#Definimos una clase productor que hereda de la clase Thread
class Productor(threading.Thread):
    #Definimos el metodo constructor
    def __init__(self, nombre):
        #Inicializamos la clase padre
        super().__init__()
        #Asignamos el nombre del productor
        self.nombre = nombre
    
    def run(self):
        global buffer

        while True:
            elemento = random.randint(1, 100)   #Genereamos un elemento aleatorio entre 1 y 100 para agregar al buffer

            #obtenemos el lock del buffer para poder agregar el elemento, si el lock no esta disponible, el productor se bloqueara hasta que el consumidor libere el lock
            with threading.Lock():
                if len(buffer)<capacidad_buffer:
                    buffer.append(elemento)
                    print(f"Productor {self.nombre} agrego {elemento} al buffer")
                    print(f"Buffer: {buffer}")
                else:
                    print(f"Buffer lleno productor {self.nombre} esperando a que el consumidor libere espacio")
        
            time.sleep(random.random())   #esperamos un tiepo aleatorio antes de generar el siguiente elemento


#Definimos una clase consumidor que hereda de la clase Thread
class Consumidor(threading.Thread):
    #Definimos el metodo constructor
    def __init__(self, nombre):
        #Inicializamos la clase padre
        super().__init__()
        #Asignamos el nombre del consumidor
        self.nombre = nombre
    
    def run(self):
        global buffer

        while True:
            #obtenemos el lock del buffer para poder consumir un elemento, si el lock no esta disponible, el consumidor se bloqueara hasta que el productor libere el lock
            with threading.Lock():
                if len(buffer)>0:
                    elemento = buffer.pop(0)
                    print(f"Consumidor {self.nombre} consumió {elemento} del buffer")
                    print(f"Buffer: {buffer}")
                else:
                    print(f"Buffer vacio consumidor {self.nombre} esperando a que el productor agregue elementos")
        
            time.sleep(random.random())   #esperamos un tiepo aleatorio antes de generar el siguiente elemento