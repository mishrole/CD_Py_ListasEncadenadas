class Node:
    listaNodos = []
    def __init__( self, nombre, apellido, id ):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.next = None
        Node.listaNodos.append( self )

    def getId( self ):
        return self.id
    
    @classmethod
    def allNodes( cls ):
        for nodo in cls.listaNodos:
            print(nodo.nombre, nodo.apellido, str(nodo.id))