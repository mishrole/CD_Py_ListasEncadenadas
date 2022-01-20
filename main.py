from Node import Node
from ListaEncadenada import ListaEncadenada

listaPersonas = ListaEncadenada()
persona1 = Node("Alex", "Martinez", 123)
persona2 = Node("Martha", "Sánchez", 456)
persona3 = Node("Mitchell", "Rodríguez", 457)
persona4 = Node("Miguel", "López", 789)

# Head de la lista
listaPersonas.insertarNodo( persona1 )
# Segundo nodo de la lista
listaPersonas.insertarNodo( persona2 )
# Tercer nodo de la lista
listaPersonas.insertarNodo( persona3 )
# Último nodo de la lista
listaPersonas.insertarNodo( persona4 )

# listaPersonas.imprimeLista()

# listaPersonas.eliminaNodo(123)
listaPersonas.eliminaNodo(456)
# listaPersonas.eliminaNodo(789)

listaPersonas.imprimeLista()