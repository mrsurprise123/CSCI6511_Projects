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
        newVertex = Vertex(vertexIndex, vertexSquare)
        if len(cls.vertices) == vertexIndex:
            cls.vertices.append(newVertex)
        else:
            print('Can not add this new vertex, because it is not inputted in order!')
    
    def setPathcost(self,pathCost):
        self.pathCost = pathCost
    
    def getPathcost(self):
        return self.pathCost
    
    def getfValue(self):
        return self.fValue
    
    def setfValue(self,fvalue):
        self.fValue = fvalue
    
    def getgValue(self):
        return self.gValue
    
    def setgValue(self,gValue):
        self.gValue = gValue
    
    def getvertexIndex(self):
        return self.vertexIndex
    
    def getvertexSquare(self):
        return self.vertexSquare
    
    @classmethod
    def getVertex(cls,vertexIndex):
        return cls.vertices[vertexIndex]

    @classmethod
    def clearVertices(cls):
        cls.vertices.clear()

# class to represent the edges
class Edge:
    def __init__(self,fromIndex,toIndex,edgeCost):
        self.fromIndex = fromIndex
        self.toIndex = toIndex
        self.edgeCost = edgeCost
    
    def getfromIndex(self):
        return self.fromIndex
    def gettoIndex(self):
        return self.toIndex
    def getedgeCost(self):
        return self.edgeCost
    
    def hashcode(self):
        pass
    
    def equal(self,edge):
        pass

# class to represent the graph
class Graph:
    def __init__(self, vertexCount):
        self.vertexCount = vertexCount
        self.edgeCount = 0
        self.graph = []
        for i in range(vertexCount):
            self.graph.append([])
    
    def getvertexCount(self):
        return self.vertexCount
    def getedgeCount(self):
        return self.edgeCount
    
    def addEdge(self, fromIndex, toIndex, edgeCost):
        self.graph[fromIndex].append(Edge(fromIndex, toIndex, edgeCost))
        self.graph[toIndex].append(Edge(toIndex,fromIndex,edgeCost))
        self.edgeCount += 1
    
    def getedgeCost(self, fromIndex, toIndex):
        for e in self.graph[fromIndex]:
            if e.gettoIndex == toIndex:
                return e.getedgeCost()
        return -1




