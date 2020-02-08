print('hello world')

list1 = [1,2,3,4,5]
print(len(list1))

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

    def Dji():
        Dist=[[] for i in range(self.maxSize)] #存储源点到每一个终点的最短路径的长度
        Path=[[] for i in range(self.maxSize)] #存储每一条最短路径中倒数第二个顶点的下标
        flag=[0 for i in range(self.maxSize)] #记录每一个顶点是否求得最短路径
        index=0
        #初始化
        while index < self.maxSize:
                Dis[index] = self.graph.getedgeCost(self.fromIndex,index)
                if self.graph.getedgeCost(self.fromIndex,index)<float('inf'): #正无穷
                    Path[index]=self.fromIndex
                else:
                    Path[index]=-1 #表示从顶点Vertex到index无路径
            index+=1
        flag[Vertex]=1
        Path[Vertex]=0
        Dist[Vertex]=0
        index=1
        while _ < self.maxSize - 1:
            MinDist=float('inf')
            j=0
            while j<self.maxSize:
                if flag[j]==0 and Dist[j]<MinDist:
                    tVertex=j #tVertex为目前从V-S集合中找出的距离源点Vertex最断路径的顶点
                    MinDist=Dist[j]
                j+=1
            flag[tVertex]=1
            EndVertex=0
            MinDist=float('inf') #表示无穷大，若两点间的距离小于MinDist说明两点间有路径
            #更新Dist列表，符合思想中第三条
            while EndVertex<self.VertexNum:
                if flag[EndVertex]==0:
                    if self.graph.getedgeCost(tVertex,EndVertex)<MinDist and Dist[tVertex]+self.graph.getedgeCost(tVertex,EndVertex)<Dist[EndVertex]:
                        Dist[EndVertex]=Dist[tVertex]+self.graph.getedgeCost(tVertex,EndVertex)
                        Path[EndVertex]=tVertex
                EndVertex+=1
            index+=1
        vertex_endnode_path=[] #存储从源点到终点的最短路径
        return Dist[EndNode],start_end_Path(Path,Vertex,EndNode,vertex_endnode_path)

    def start_end_Path(Path,start,endnode,path):
        if start==endnode:
            path.append(start)
        else:
            path.append(endnode)
            start_end_Path(Path,start,Path[endnode],path)
            return path