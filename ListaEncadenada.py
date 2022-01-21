from Node import Node

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
        print("\nLista de Nodos\n- - - - - - - - - - - -")

        if self.head == None:
            print("La lista está vacía")

        # aux es la cabeza del nodo
        aux = self.head

        # Mientras (while) next tiene algo (no es None), imprimimos aux y nos movemos a ese nodo
        while aux != None:
            print(aux.nombre, aux.apellido, str(aux.id))
            aux = aux.next
        
    def buscarNodo( self, id ):
        if self.head == None:
            print("La lista está vacía")
            return None

        aux = self.head
        result = None

        while aux != None:
            if aux.getId() == id:
                result = aux
                break

            aux = aux.next

        print("\nResultado de búsqueda\n- - - - - - - - - - - -")
        
        if result != None:
            print(f"{result.nombre} {result.apellido}, {str(result.id)}")
        else:
            print("No se encontró un nodo con ese Id")

        return result

    def eliminaNodo( self, id ):
        result = None

        print("\nEliminar nodo\n- - - - - - - - - - - -")
        if self.head == None:
            print("La lista está vacía")
            return result

        # Si es 1, Head pasa al segundo
        aux = self.head
        prev = None

        while aux != None:
            # aux es el nodo buscado
            if aux.getId() == id:
                # print(f"\nNodo a eliminar: {aux.nombre}")
                # Nodo encontrado es la cabeza
                if prev == None:
                    # print(f"Cabeza: {aux.nombre}")
                    self.head = aux.next
                    result = aux
                    break

                # Nodo encontrado es la colita
                if aux.next == None:
                    # print(f"Colita: {aux.nombre}")
                    if prev != None:
                        prev.next = None
                        result = aux
                        break
                
                # Nodo encontrado está entre la cabeza y la colita
                if aux.next != None and prev != None:
                    # print(f"Medio: {aux.nombre}")
                    prev.next = aux.next
                    result = aux
                    break
                
            prev = aux
            aux = aux.next
        
        if result != None:
            print(f"Nodo con Id {result.getId()} eliminado")

    def insertaNodoEnPosicion( self, nuevoNodo, indice ):
        # Hacer un conteo de los nodo actuales en la lista
        # Validar el índice contra el conteo. 
        # En caso en el que el índice es mayor al conteo, retorno None
        # De lo contrario insertar el nodo y retornar un mensaje de éxito
        result = None

        print("\nAñadir nodo en posición\n- - - - - - - - - - - -")

        if self.head == None:
            print("La lista está vacía")
            return result

        # totalAux = self.head
        totalIndices = len(Node.listaNodos)

        aux = self.head
        prev = None
        contador = 0

        # while totalAux != None:
        #     totalIndices += 1
        #     totalAux = totalAux.next

        if indice <= totalIndices:
            while aux != None:
                contador += 1
                # Es el nodo buscado
                if contador == indice:
                    # Es cabeza
                    if prev == None:
                        nuevoNodo.next = self.head
                        self.head = nuevoNodo
                        result = nuevoNodo
                        break
                    
                    # Es colita
                    if aux.next == None and prev != None:
                        nuevoNodo.next = prev.next
                        prev.next = nuevoNodo
                        aux.next = None
                        result = nuevoNodo
                        break

                    # Entre cabeza y colita
                    if aux.next != None and prev != None:
                        nuevoNodo.next = prev.next
                        prev.next = nuevoNodo
                        result = nuevoNodo
                        break


                prev = aux
                aux = aux.next

        
        if result != None:
            print(f"Nodo con Id {result.getId()} insertado de manera exitosa en posición {indice}")

        return result
