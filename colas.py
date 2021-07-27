#Implementacion de COLAS en Python basico y sencillo para ERDD con FIFO

cola = ["Maria", "Dario","Ramon","Lola"] #Creacion de COLA con 4 elementos
print('En la cola de la tienda estan: ') #Imprimimos COLA
print(cola) 

#Agregamos elementos al final de la COLA
print('Agregamos a Karla y Jean a la cola de la tienda')
cola.append("Karla") #Agregamos Karla a COLA
cola.append("Jean") #Agregamos Jean a COLA

print('La cola completa seria: ')
print(cola) #Mostramos la COLA con las personas recien llegadas a la tienda

#Sacando elementos al Inicio de la COLA
s = cola.pop(0) #Sacara el primer elemento de la COLA y lo guardara en s
print("El usuario ya atendido es: ", s) #Mostramos a s que es el primer elemento de la COLA y es el primero en salir
print("Ahora saldra de la cola porque ya",s,"fue atendida") 

print('La cola quedaria asi: ')
print(cola) #Imprimira la COLA sin el primer elemento en este caso, Maria