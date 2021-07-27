#Dos Filas en el Cine, entra siempre la persona que es mayor y si tienen edad iguales entra la persona fila 1
#Creamos las 2 colas en el Cine con nombre COLA 1 y COLA 2, 3 Integrantes en la 1 y 4 en la 2
#Creamos otras 2 colas con nombres EDAD 1 y EDAD 2, donde guardaremos las EDADES de los sujetos respectivamente

cola1 = ["Maria", "Dario","Ramon"] #Creacion de COLA 1 con 3 elementos
edad1 = [17,23,28] #Creacion de EDAD 1 con edades de los integrantes de cola 1
cola2 = ["Carlos", "Kate","Tyler","Sara"] #Creacion de COLA 2 con 4 elementos
edad2 = [20,25,39,18] #Creacion de EDAD 2 con edades de los integrantes de cola 2

#Impresion de ambas colas con respectivas edades
print('En la fila 1 tenemos a: ') #Imprimimos COLA 1
print(cola1) 
print('Con edades de: ') #Imprimimos las edades de los integrantes de COLA 1
print(edad1)
print('En la fila 2 estan: ') #Imprimimos COLA 2
print(cola2)
print('Con edades de: ') #Imprimimos las edades de los integrantes de COLA 2
print(edad2)

#Supongamos que llegan 3 personas mas, 2 a COLA 1 Y la otra a COLA 2
#Agregamos elementos al final de la COLA 1 y 2
print('Agregamos a Karla y Jean a la fila 1 del cine y a Lucia a la fila 2')
cola1.append("Karla") #Agregamos Karla a COLA 1
cola1.append("Jean") #Agregamos Jean a COLA 1
cola2.append("Lucia") #Agregamos Lucia a COLA 2
#Agregamos sus edades a EDAD 1 y EDAD 2 respectivamente
edad1.append(21) #Edad de Karla
edad1.append(34) #Edad de Jean
edad2.append(19) #Edad de Lucia

#Imprimimos la COLA 1 y EDAD 1
print('En la fila 1 tenemos a: ') #Imprimimos COLA 1
print(cola1) 
print('Con edades de: ') #Imprimimos las edades de los integrantes de COLA 1
print(edad1)

#Imprimimos la COLA 2 y EDAD 2
print('En la fila 1 tenemos a: ') #Imprimimos COLA 2
print(cola2) 
print('Con edades de: ') #Imprimimos las edades de los integrantes de COLA 2
print(edad2)

#Entrada al Cine por FILA y EDAD
print('Al cine solo entrara el elemento mayor de ambas filas, si tienen edades iguales entra el de la FILA 1 Primero')
if edad1 [0] > edad2 [0]:
    print('A la sala de cine entrara', cola1 [0], 'primero que', cola2 [0],'porque',edad1 [0],'es mayoe que' ,edad2 [0])
elif edad1 == edad2:
    print('A la sala de cine entrara', cola1 [0], 'primero que', cola2 [0], 'ya que la prioridad la ttiene la FILA 1')
else:
    print('A la sala de cine entrara', cola2 [0], 'primero que', cola1 [0])

#Como Carlos entra a la sala debemos de eliminarlo de la COLA2 
entro = cola2.pop(0) #Sacamos a Carlos y lo guardamos en entro
print('El usuario que entro a la sala fue: ', entro)
#Me gusto mucho este programa, hay cosas a mejorar pero el tiempo ya no me dara para hacer las mejoras, 
#igualmente alegre de poder utilizar los metodos aprendidos en clase, estoy aprendiendo a usar py, un saludo Profesora