# Productores-y-consumidores

El link a mi repositorio es: [GitHub](https://github.com/crltsnch/Productores-y-consumidores)

# En que consiste

Este ejercicio consiste en que el productor aporta unos elementos y el consumidor hace uso de esos elementos, el problema está en si el productor provee más rápido de lo que el consumidor puede aceptar o si el consumidor consume más rápido que lo que el productor puede aportar.
Este problema lo resolvemos con una gestión correcta de los recursos en equilibrio (sincronización entre consumidor y productor) para evitar interbloqueo o exclusión mutua. Yo lo he resuelto con hilos y para asegurar que solo un hilo acceda al buffer he utilizado el objeto lock.

# Archivo `productorconsumidor.py`

```
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
```

# Archivo `main.py`

```
from productorconsumidor import *

#Creamos 3 productores y 3 consumidores
def main():
    #Creamos una lista para almacenar los productoes y los consumidores
    productores = []
    consumidores = []

    #Creamos 3 productores y 3 consumidores y los agregamos a sus respectivas listas
    for i in range(3):
        productor = Productor(f"{i+1}")
        productores.append(productor)

        consumidor = Consumidor(f"{i+1}")
        consumidores.append(consumidor)
    
    #Inicializamos los hilos de los productores y los consumidores
    for p in productores:
        p.start()
    for c in consumidores:
        c.start()

    #Esperamos a que los hilos terminen su ejecución
    for p in productores:
        p.join()
    for c in consumidores:
        c.join()


if __name__ == "__main__":
    main()

```

