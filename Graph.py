# Graph Theory
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        else:
            self.gdict = gdict
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            dequeue = queue.pop(0)
            print(dequeue)
            for adjacentVertex in self.gdict[dequeue]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            deStack = stack.pop()
            print(deStack)
            for adjacentVertex in self.gdict[deStack]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)


customDict = {  "a" : ["b","c"],
                "b" : ["a","d","e"],
                "c" : ["a","e"],
                "d" : ["b","e","f"],
                "e" : ["b","c","d"],
                "f" : ["d","e"]
                }
graph = Graph(customDict)
graph.addEdge("e", "f")
graph.bfs("a")
graph.dfs("a")
print(graph.gdict)
