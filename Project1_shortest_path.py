# This is the Python project for CSCI66511
# @author Yihan chen
from queue import PriorityQueue
import math
import time

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
    
    def __lt__(self, other):
        return self.pathCost < other.pathCost

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

# class to repersent the uniform cost search

class UniformCostSearch:
    def __init__(self, graph, fromIndex, toIndex, maxSize):
        self.marked = [False for i in range(graph.getvertexCount())]
        self.edgeTo = [0 for i in range(graph.getedgeCount())]
        self.fromIndex = fromIndex
        self.toIndex = toIndex
        self.bfs(graph, maSize)
    
    def bfs(self,graph, maxSize):
        Vertex.getVertex(self.fromIndex).setPathcost(0)
        queue = PriorityQueue(maxSize)
        queue.put(Vertex.getVertex(self.fromIndex))
        foundPath = False

        while queue.empty() == False and not foundPath:
            currentVertex = queue.get()
            self.marked[currentVertex.getvertexIndex()] = True

            if currentVertex.getvertexIndex == self.toIndex:
                foundPath = True
            
            for edge in graph.graph[currentVertex.getvertexIndex()]:
                neighbor = edge.gettoIndex()
                pathcost = edge.getPathcost()
                neighborVertex = Vertex.getVertex(neighbor)
                if not self.marked[neighbor] and not neighborVertex in queue:
                    neighborVertex.setPathcost(currentVertex.getPathcost + pathcost)
                    self.edgeTo[neighbor] = currentVertex.getvertexIndex()
                    queue.put(neighborVertex)
                elif neighborVertex in queue and neighborVertex.getPathcost() > currentVertex.getPathcost + pathcost:
                    self.edgeTo[neighbor] = currentVertex.getvertexIndex()
                    neighborVertex.setPathcost(currentVertex + pathcost)
                    queue.remove(neighborVertex)
                    queue.put(neighborVertex)
    
    def hasPathTo(self,vertex):
        return self.marked[vertex]
    
    def pathTo(self, vertex):
        if not self.hasPathTo(vertex):
            return null
        path = []
        x = vertex
        while x != self.fromIndex:
            path.append(x)
            x = self.edgeTo(x)
        path.append(self.fromIndex)
        return path

# class to repersent the A* algorithm
class AStar:
    def __init__(self, graph, fromIndex, toIndex, maxSize):
        self.marked = [False for i in range(graph.getvertexCount())]
        self.edgeTo = [0 for i in range(graph.getedgeCount())]
        self.fromIndex = fromIndex
        self.toIndex = toIndex
        self.astar(graph, maSize)
    
    def astar(self, graph, maxSize):
        Vertex.getVertex(self.fromIndex).setPathcost(0)
        Vertex.getVertex(self.fromIndex).setfValue(heuristic(self.fromIndex, self.toIndex))
        queue = PriorityQueue(maxSize)
        queue.put(Vertex.getVertex(self.fromIndex))
        foundPath = False

        while queue.empty() == False and not foundPath:
            currentVertex = queue.get()
            self.marked[currentVertex.getvertexIndex()] = True

            if currentVertex.getvertexIndex == self.toIndex:
                foundPath = True
            
            for edge in graph.graph[currentVertex.getvertexIndex()]:
                neighbor = edge.gettoIndex()
                if self.marked[neighbor]:
                    continue

                neighborVertex = Vertex.getVertex(neighbor)
                tentativeGValue = currentVertex.getgValue() + edge.getedgeCost()
                estimatedFScore = tentativeGValue + heuritic(neighborVertex, self.toIndex)

                if not self.marked[neighbor] and not neighborVertex in queue:
                    self.edgeTo[neighbor] = currentVertex.getvertexIndex()
                    neighborVertex.setfValue(estimatedFScore)
                    neighborVertex.setgValue(tentativeGValue)
                    queue.put(neighborVertex)
                elif neighborVertex in queue and estimatedFScore < neighborVertex.getfValue:
                    self.edgeTo[neighbor] = currentVertex.getvertexIndex()
                    neighborVertex.setfValue(estimatedFScore)
                    neighborVertex.setgValue(tentativeGValue)
                    queue.remove(neighborVertex)
                    queue.put(neighborVertex)
    
    def heuristic(vertex1, vertex2):
        v1 = Vertex.getVertex(vertex1)
        v2 = Vertex.getVertex(vertex2)

        x = abs((v1.getvertexSquare / 10) - (v2.getvertexSquare / 10)) - 1
        y = abs((v1.getvertexSquare % 10) - (v2.getvertexSquare % 10)) - 1

        if x >= 0:
            if y >= 0:
                return sqrt(math.pow(x,2) + math.pow(y,3)) * 100
            else:
                return x * 100
        else:
            if y >= 0:
                return y * 100
            else:
                return 0

    
    def hasPathTo(self,vertex):
        return self.marked[vertex]
    
    def pathTo(self, vertex):
        if not self.hasPathTo(vertex):
            return null
        path = []
        x = vertex
        while x != self.fromIndex:
            path.append(x)
            x = self.edgeTo(x)
        path.append(self.fromIndex)
        return path

def generateGraph(vertexNumber,file):
    isVertex = True
    graph = Graph(vertexNumber)

    for line in file.readlines():
        if line[0] == '#' or line == 'Vertices':
            continue
        if line == 'Edges':
            isVertex = False
            continue
        elements = line.split(",",)
        if isVertex:
            Vertex.addVertex(int(elements[0]), (int(elements[1])) * 10 + (int(elements[2])))
        else:
            graph.addEdge(int(elements[0]), int(elements[1]),int(elements[2]))
    
    return graph

def showPath(graph, path, isinformed):
    if isinformed:
        print("Result for informed search:")
    else:
        print("Result for uninformed search:")

    PathCost = 0
    currentV = path.pop()
    print(currentV + '-->')
    while not path.empty():
        lastV = currentV
        currentV = path.pop()
        cost = graph.getedgeCost(last,currentV)
        if cost == -1:
            print("can not find the edge from vertex" + lastV + "to" + currentV)
        PathCost += cost
        print(currentV)
        if path.empty():
            break
        print("-->")
    print("Pathcost is " + PathCost)


def uninformed(graph, fromIndex, toIndex, vertexNumber):
    start = time.time()
    ucs = UniformCostSearch(graph, fromIndex, toIndex, vertexNumber)
    if ucs.hasPathTo(toIndex):
        showPath(graph,ucs.pathTo(toIndex),False)
    else:
        print("There is no path to " + toIndex)
    end = time.time()
    print("Time for uninformed is " + end)

def informed(graph, fromIndex, toIndex, vertexNumber):
    start = time.time()
    astar = AStar(graph, fromIndex, toIndex, vertexNumber)
    if astar.hasPathTo(toIndex):
        showPath(graph,astar.pathTo(toIndex),True)
    else:
        print("There is no path to " + toIndex)
    end = time.time()
    print("Time for informed is " + end)





def main():
    filename = input("Please input the file name")
    fromIndex = input("Please input the fromIndex")
    toIndex = input("Please input the ToIndex")

    file = open(filename)
    vertexNumber = int(filename[5,filename.find('_')])

    graph = generateGraph(vertexNumber,file)

    uninformed(graph, fromIndex, toIndex, vertexNumber)
    informed(graph, fromIndex, toIndex, vertexNumber)
    Vertex.clearVertices()
    file.close()

if __name__ == '__main__':
    main()









