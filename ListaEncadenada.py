# from Node import Node

# La lista inicialmente está vacía
class ListaEncadenada:
    def __init__( self ):
        self.head = None

    def insertarNodo( self, nuevoNodo ):
        # Si la lista está vacía, el nodo debe ser Head
        if self.head == None:
            self.head = nuevoNodo
        # Si la lista ya tiene elementos
        else:
            # Recorre la lista hasta el final (es un objeto, no hay índice)
            # aux es la cabeza del nodo
            aux = self.head

            # Mientras (while) next tiene algo (no es None), nos movemos a ese nodo
            while aux.next != None:
                aux = aux.next

            # Si next es None, se enlaza el nuevo nodo
            aux.next = nuevoNodo
    
    def imprimeLista( self ):
        print("Lista de Nodos\n- - - - - - - - - - - -")

        # aux es la cabeza del nodo
        aux = self.head

        # Mientras (while) next tiene algo (no es None), imprimimos aux y nos movemos a ese nodo
        while aux != None:
            print(aux.nombre, aux.apellido, str(aux.id))
            aux = aux.next

    def eliminaNodo (self, id):
        # Si es 1, Head pasa al segundo
        aux = self.head
        prev = None

        while aux != None:
            # aux es el nodo buscado
            if aux.id == id:
                print(f"Nodo a eliminar: {aux.nombre}")
                # Nodo encontrado es la cabeza
                if prev == None:
                    # print(f"Cabeza: {aux.nombre}")
                    self.head = aux.next
                    break

                # Nodo encontrado es la colita
                if aux.next == None:
                    # print(f"Colita: {aux.nombre}")
                    if prev != None:
                        prev.next = None
                        break
                
                # Nodo encontrado está entre la cabeza y la colita
                if aux.next != None and prev != None:
                    # print(f"Medio: {aux.nombre}")
                    prev.next = aux.next
                    break
                
            prev = aux
            aux = aux.next
