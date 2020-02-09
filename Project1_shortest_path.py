# This is the Python project for CSCI66511
# @author Yihan chen
from queue import PriorityQueue
import math
import time
global Maxnumber
Maxnumber = 99999999999999
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
        return self.fValue < other.fValue
    # def __gt__(self, other):
    #     return self.fValue > other.fValue

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
    
    def setfValue(self,fValue):
        self.fValue = fValue
    
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
    def getedges(self,vertex):
        return self.graph[vertex]
    def getedgeCost(self, fromIndex, toIndex):
        for e in self.graph[fromIndex]:
            if e.toIndex == toIndex:
                return e.edgeCost
        return Maxnumber

# class to repersent the uniform cost search

class UniformCostSearch:
    def __init__(self, graph, fromIndex, toIndex, maxSize):
        self.fromIndex = fromIndex
        self.toIndex = toIndex
        self.graph = graph
        self.maxSize = maxSize
        self.path = self.dijkstra()
    
    def dijkstra(self):
        shortest_paths = {self.fromIndex: (None,0)}
        current_node = self.fromIndex
        visited = set()

        while current_node != self.toIndex:
            visited.add(current_node)
            destinations = self.graph.getedges(current_node)
            weight_to_current_node = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = self.graph.getedgeCost(current_node,next_node.toIndex) + weight_to_current_node
                if next_node.toIndex not in shortest_paths:
                    shortest_paths[next_node.toIndex] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node.toIndex][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node.toIndex] = (current_node, weight)

            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return "There is no route to " + str(self.toIndex)
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
        
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node
        # Reverse path
        path = path[::-1]
        return path


# class to repersent the A* algorithm
class AStar:
    def __init__(self, graph, fromIndex, toIndex, maxSize):
        self.marked = [False for i in range(graph.getvertexCount())]
        self.edgeTo = [None for i in range(graph.getedgeCount())]
        self.fromIndex = fromIndex
        self.toIndex = toIndex
        self.astar(graph, maxSize)
    
    def astar(self, graph, maxSize):
        Vertex.getVertex(self.fromIndex).setfValue(int(self.heuristic(self.fromIndex, self.toIndex)))
        # print(Vertex.getVertex(self.fromIndex).fValue)
        queue = PriorityQueue(maxSize)
        queueContains = [False for i in range(graph.getvertexCount())]
        queue.put(Vertex.getVertex(self.fromIndex))
        queueContains[self.fromIndex] = True
        foundPath = False

        while queue.empty() == False and not foundPath:
            currentVertex = queue.get()
            print(currentVertex.vertexIndex,end=' ')
            print(currentVertex.fValue, end=' ')
            print(currentVertex.gValue)
            queueContains[currentVertex.getvertexIndex()] = False
            self.marked[currentVertex.getvertexIndex()] = True

            if currentVertex.getvertexIndex == self.toIndex:
                foundPath = True
            for edge in graph.graph[currentVertex.getvertexIndex()]:
                neighbor = edge.toIndex
                if self.marked[neighbor]:
                    continue
                neighborVertex = Vertex.getVertex(neighbor)
                GValue = currentVertex.getgValue() + edge.edgeCost
                FValue = GValue + int(self.heuristic(neighbor, self.toIndex))
                if not queueContains[neighbor]:
                    self.edgeTo[neighbor] = currentVertex.getvertexIndex()
                    neighborVertex.setfValue(FValue)
                    neighborVertex.setgValue(GValue)
                    queue.put(neighborVertex)
                    queueContains[neighbor] = True
                elif queueContains[neighbor] and FValue < neighborVertex.gValue:
                    self.edgeTo[neighbor] = currentVertex.getvertexIndex()
                    neighborVertex.setfValue(FValue)
                    neighborVertex.setgValue(GValue)
                    tempqueue = PriorityQueue(maxSize)
                    while queue.empty() == False:
                        temp = queue.get()
                        if temp.getvertexIndex() == neighbor:
                            continue
                        tempqueue.put(temp)
                    # queue.remove(neighborVertex)
                    # while tempqueue
                    queue = tempqueue
                    queue.put(neighborVertex)
    
    def heuristic(self,vertex1, vertex2):
        v1 = Vertex.getVertex(vertex1)
        v2 = Vertex.getVertex(vertex2)
        x = abs(int((v1.getvertexSquare() / 10)) - int((v2.getvertexSquare() / 10))) - 1
        y = abs((v1.getvertexSquare() % 10) - (v2.getvertexSquare() % 10)) - 1

        if x >= 0:
            if y >= 0:
                return math.sqrt(math.pow(x,2) + math.pow(y,2)) * 100
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
            x = self.edgeTo[x]
        path.append(self.fromIndex)
        return path

def generateGraph(vertexNumber,file):
    isVertex = True
    graph = Graph(vertexNumber)

    for line in file.readlines():
        if line[0] == '#' or line == 'Vertices\n':
            continue
        if line == 'Edges\n':
            isVertex = False
            continue
        elements = line.split(",")
        if isVertex:
            Vertex.addVertex(int(elements[0]), int(elements[1]) * 10 + int(elements[2]))
            # temp = int(elements[1]) * 10 + int(elements[2])
            # print(str(elements[0]) + " " + str(temp))
        else:
            graph.addEdge(int(elements[0]), int(elements[1]),int(elements[2]))
    
    # for i in range(vertexNumber):
    #     for e in graph.graph[i]:
    #         print("Edge:" + str(e.fromIndex) + " " + str(e.toIndex) + " " + str(e.edgeCost))

    return graph

def showPath(graph, path):
    print("Result for informed search:")
    PathCost = 0
    currentV = path.pop()
    print(str(currentV) + '-->',end='')
    while len(path) != 0:
        lastV = currentV
        currentV = path.pop()
        cost = graph.getedgeCost(lastV,currentV)
        if cost == Maxnumber:
            print("can not find the edge from vertex" + lastV + "to" + currentV)
        PathCost += cost
        print(currentV,end='')
        if len(path) == 0:
            break
        print("-->",end='')
    print('')
    print("Pathcost is " + str(PathCost))

def main():
    filename = input("Please input the file name ")
    fromIndex = int(input("Please input the fromIndex "))
    toIndex = int(input("Please input the ToIndex "))

    file = open(filename)
    str = filename.split('_')
    vertexNumber = int(str[0][5:])
    graph = generateGraph(vertexNumber,file)


    # uninformed search
    start = time.time()
    ucs = UniformCostSearch(graph, fromIndex, toIndex, vertexNumber)
    print(ucs.path)
    end = time.time()
    print("Time for uninformed is ")
    print(end)

    # informed search
    start = time.time()
    astar = AStar(graph, fromIndex, toIndex, vertexNumber)
    if astar.hasPathTo(toIndex):
        showPath(graph,astar.pathTo(toIndex))
    else:
        print("There is no path to ")
        print(toIndex)
    end = time.time()
    print("Time for informed is ")
    print(end)

    Vertex.clearVertices()
    file.close()

if __name__ == '__main__':
    main()









