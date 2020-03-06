"""
Graph Implementation in Python
"""
class Graph:
    def __init__(self):
        self.graph = {}
      
    def add_edge(self, node, neighbor=None):
        edges = []
        if neighbor != None:
          if node not in self.graph:
              edges.append(neighbor)
              self.graph[node] = edges
              self.add_edge(neighbor, node)
          if node in self.graph:
              edges = self.graph[node]
              if neighbor not in edges:
                  edges.append(neighbor)
        else:
          if node not in self.graph:
              self.graph[node] = edges
    def print_graph(self):
        return self.graph
    def show_vertices(self, mode):
        keys = []
        keys = self.graph.keys()
        return keys
    def show_edges(self, node):
        return node, self.graph[node]
    

a = Graph()
a.add_edge("A")
a.add_edge("D")
print(a.print_graph())
a.add_edge("B", "A")
print(a.print_graph())
a.add_edge("C", "A")
print(a.print_graph())


