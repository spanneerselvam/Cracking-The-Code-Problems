"""
4-2: Design an algorithm to find out whether there is a route between two nodes.
Look at edge_exists() method
"""
class DirectedGraph:
    def __init__(self):
        self.graph = {}
    """
    add_edge(a, b) will be {a:b, b:[]}
    """
    def add_edge(self, node, neighbor=None):
        edges = []
        if neighbor != None:
          if node not in self.graph:
              edges.append(neighbor)
              self.graph[node] = edges
             # self.add_edge(neighbor, node) #don't need to add the nodes for the neighbors
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
    def edge_exists(self, node, node1):
        edges = []
        edges1 = []
        if node not in self.graph or node1 not in self.graph:
            return False
        else:
            edges = self.graph[node]
            edges1 = self.graph[node1]
            for x in edges:
                if node1 == x:
                    return True
            for y in edges1:
                if node == y:
                    return True
        return False

a = Graph()
a.add_edge("A")
print(a.print_graph())
a.add_edge("B", "A")
print(a.print_graph())
a.add_edge("C", "A")
print(a.print_graph())
print(a.edge_exists("B", "C"))
print(a.edge_exists("A", "C"))
print(a.edge_exists("A", "D"))
