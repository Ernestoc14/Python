# Implementacion de Pilas en Python Basico y Sencillo para ERDD con LIFO

pila = [1,2,3] #Creacion de PILA con tres elementos
print('La pila es:') #Impresion de PILA
print(pila)

#Agregamos elementos por el final
print ('Agregamos los numeros 4 y 5 a la Pila')
pila.append(4) #Agregamos el elemento 4 a la PILA
pila.append(5) #Agregamos el elemento 5 a la PILA

print('La pila con los numeros 4 y 5 agregados es: ')
print(pila) #Imprimimos la PILA que mostrara los elementos tambien agregados, 4 y 5

#Sacamos elementos por el Final
s = pila.pop() #Sacara el ultimo elemento de la PILA y lo guardara en s
print( "Sacando el elemento",s ) #Mostramos el numero que fue extraido de la PILA

print('La pila quedaria asi: ')
print(pila) #Imprimira la PILA sin el untimo elemento porque ha sido sacado