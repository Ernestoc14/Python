#Parcial 2 ABB Dev: Ernesto Crespo

class Node:
	def __init__(self, key):
		self.left = None    #Creacion de Nodo Izq
		self.right = None   #Creacion de Nodo Der
		self.val = key      #Aqui entra el dato

#Funcion de entrada
def insert(root, key):
	if root is None:       
		return Node(key)   
	else:                     
		if root.val == key:   
			return root          
		elif root.val < key:  
			root.right = insert(root.right, key)   
		else:                 
			root.left = insert(root.left, key)    
	return root            

#Funcion de busqueda donde tenemos como parametros la raiz y el dato
def search(root,key):
	if root is None or root.val == key: 
		return root                     

	if root.val < key:                   
		return search(root.right,key)    

	return search(root.left,key)          

#Funcion inorder donde se lleva la Raiz como parametro
def inorder(root):     #RECORRIDO INORDEN
	if root:                #Si la raiz existe entonces
		inorder(root.left)  #Imprime el lado Izquierdo
		print(root.val)     #Imprime el valor de la Raiz
		inorder(root.right) #Imprime el lado Derecho

#ABB FORMA DEL ARBOL
# 50, 48, 70, 30, 65, 90, 98,67, 20, 66, 25, 32, 69, 35, 15, 94, 99, 31.
#                     50
#           /                  \
#         48	                70
#         /                   /      \
#        30                  65        90       
#      /    \                  \          \ 
#    20     32                 67          98
#   /  \   /  \                /  \       /   \      
# 15   25 31   35             66   69    94   99        Nivel 4  


r = Node(50)       #RAIZ
r = insert(r, 48)  #IZQ
r = insert(r, 30)  #IZQ
r = insert(r, 20)  #IZQ
r = insert(r, 32)  #IZQ
r = insert(r, 15)  #IZQ HOJA
r = insert(r, 25)  #IZQ HOJA
r = insert(r, 31)  #IZQ HOJA
r = insert(r, 35)  #IZQ HOJA

r = insert(r, 70)  #DER
r = insert(r, 65)  #DER
r = insert(r, 90)  #DER
r = insert(r, 67)  #DER
r = insert(r, 98)  #DER
r = insert(r, 66)  #DER HOJA
r = insert(r, 69)  #DER HOJA 
r = insert(r, 94)  #DER HOJA
r = insert(r, 99)  #DER HOJA

# Print del arbol en Inorden 
print('El Arbol en recorrido Inorden es el siguiente: ') #Imprimimos inorden
inorder(r)
print('El nivel del arbol es: 4 ') #Nivel del Arbol
print('Las hojas del arbol son: 15 , 25 , 31 , 35') #Hojas del Arbol
print('Del lado Izquierdo')
print('Y del lado Derecho: 66 , 69 , 94 , 99')