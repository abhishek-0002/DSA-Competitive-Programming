from collections import defaultdict

class Graph:
       def __int__(self):
              self.grph =defaultdict(list)
              
       def addEdge(self,u,v):
              self.grph[u].append(v)
              
       def DFSUtil(self,v,visited):
              visted.add(v)
              print(v, end=' ')
              for neighbour in self.grph[v]:
                     if neighbour not in visited:
                            self.DFSUtil(neighbour,visited)
       def DFS(self,v):
              visited = set()
              self.DFSUtil(v,visited)

if __name__ =="__main__":
       g = Graph()
       g.addEdge(0,1)
       g.addEdge(0, 2)
       g.addEdge(1, 2)
       g.addEdge(2, 0)
       g.addEdge(2, 3)
       g.addEdge(3, 3)
       g.DFS(0)
