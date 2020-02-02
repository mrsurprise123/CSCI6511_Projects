# This is the Python project for CSCI66511
# @author Yihan chen

#class to repersents the vertices of graphs
class Vertex:
    vertices = []

    def __init__(self, vertexIndex, vertexSquare):
        self.vertexIndex = vertexIndex
        self.vertexSquare = vertexSquare
        # cost from an original vertex to this vertes
        self.pathCost = 0
        self.gValue = 0
        self.fValue = 0
    
    @classmethod
    def addVertex(cls, vertexIndex, vertexSquare):
        

