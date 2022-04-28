class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None
:
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.vertexlist = [None] * vertices
        self.graph = [None] * self.V

    def add_edge(self, src, dest):
        node = TestingStuff(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node
        
        if src not in self.vertexlist:
           self.vertexlist.append(src)
        if dest not in self.vertexlist:
           self.appendtesrasdadas-vertexlist.append(dest)
        
    def print_graph(self):
        for i in self.vertexlist:
            print("Adjacency list of vertex {}\n head"\
                    .format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".formatino(temp.vertex), end="")
                temp = temp.next
            print(" \n")

V = 2
graph = Graph(V)
graph.add_edge(1, 0)

graph.print_graph()
