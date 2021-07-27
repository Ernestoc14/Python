#Implementacion de Arbol Binario en Py Dev: Ernesto Crespo
#Creamos la clase Nodo que recibe a Key (dato que guardara)
class Node:
	def __init__(self, key):
		self.left = None    #Creacion de Nodo Izq
		self.right = None   #Creacion de Nodo Der
		self.val = key      #Aqui entra el dato

#Funcion donde entran los datos al Arbol, Raiz y Nodo Izq Der
def insert(root, key):
	if root is None:       #Si no existe la Raiz
		return Node(key)   #Devuelve el dato, siendo este la raiz
	else:                     #Si la raiz existe
		if root.val == key:   #Si el dato es igual a la raiz
			return root       #Devuelve la raiz ya que el dato la repite    
		elif root.val < key:  #Si el dato es mayor que la raiz
			root.right = insert(root.right, key)   #Dato insertado en Der
		else:                 #Si el dato es menor que la raiz
			root.left = insert(root.left, key)     #Dato insertado en Izq
	return root            #Devuelve la raiz

#Funcion de busqueda donde tenemos como parametros la raiz y el dato
def search(root,key):
	if root is None or root.val == key: #Si la raiz no existe o la raiz tiene el valor del dato
		return root                     #Devuelve la raiz

	if root.val < key:                   #Si la raiz es menor al dato
		return search(root.right,key)    #Busca por el lado derecho y devuelve el dato

	return search(root.left,key)          #Sino busca por el lado izquierdo y devuelve el dato

#Funcion inorder donde se lleva la Raiz como parametro
def inorder(root):     #RECORRIDO INORDEN
	if root:                #Si la raiz existe entonces
		inorder(root.left)  #Imprime el lado Izquierdo
		print(root.val)     #Imprime el valor de la Raiz
		inorder(root.right) #Imprime el lado Derecho

#Funcion preorder donde se lleva la Raiz como parametro
def preorder(root):      #RECORRIDO PREORDEN
	if root:                #Si la raiz existe entonces
		print(root.val)     #Imprime el valor de la Raiz
		preorder(root.left)  #Imprime el lado Izquierdo
		preorder(root.right) #Imprime el lado Derecho

#Funcion postorder donde se lleva la Raiz como parametro
def postorder(root):      #RECORRIDO POSTORDEN
	if root:                #Si la raiz existe entonces
		postorder(root.left)  #Imprime el lado Izquierdo
		postorder(root.right) #Imprime el lado Derecho
		print(root.val)     #Imprime el valor de la Raiz

#BST  FORMA DEL ARBOL
#        50
#      /    \
#    30	    70
#   /  \   /  \
# 20   40 60   80

r = Node(50)       #RAIZ
r = insert(r, 30)  #IZQ
r = insert(r, 20)  #IZQ
r = insert(r, 40)  #IZQ
r = insert(r, 70)  #DER
r = insert(r, 60)  #DER
r = insert(r, 80)  #DER

# Print inoder traversal of the BST
print('El recorrido inorden es el siguiente: ') #Imprimimos inorden
inorder(r)
print('El recorrido preorden es el siguiente: ') #Imprimimos preorden
preorder(r)
print('El recorrido postorden es el siguiente: ') #Imprimimos postorden
postorder(r)