# Construye un programa que sume 10 enteros

pila = [1,2,3,4,5] #Creacion de PILA con 5 elementos
print('La pila es:') #Impresion de PILA
print(pila)

#Agregamos elementos por el final
print ('Agregamos los numeros 6,7,8,9 y 10 a la Pila')
pila.append(6) #Agregamos el elemento 6 a la PILA
pila.append(7) #Agregamos el elemento 7 a la PILA
pila.append(8) #Agregamos el elemento 8 a la PILA
pila.append(9) #Agregamos el elemento 9 a la PILA
pila.append(10) #Agregamos el elemento 10 a la PILA

#Impresion de PILA con los agregados
print('Esta es la pila con los 10 Elementos')
print(pila) #Asi quedaria la pila con los 10 elementos

#Sumamos los 10 elementos 
suma = 1+2+3+4+5+6+7+8+9+10

#Imprimimos la suma de los 10 elementos
print( "La suma de los 10 elementos es: ",suma ) #Mostramos el suma de todos los elementos
#Imprimimos la pila
print('La Pila es: ', pila)