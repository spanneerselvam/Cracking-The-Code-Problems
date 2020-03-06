from stack import Stack
from queue import Queue
"""
Graph Data Structure Implementation with DFS and BFS 
"""
class Graph:
    def __init__(self):
        self.graph = {}
        self.s = Stack()
        self.q = Queue()
        self.visited = []
        self.seen = []
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
    """
    DFS: Push a child of a node into a stack and visit that child's children (node's grandparent)
    """
    def dfs(self, node, node1):
        children_temp = self.graph[node]
        children_temp1 = self.graph[node1]
        if node not in self.graph or node1 not in self.graph or children_temp == [] or children_temp1 == []:
          return self.visited
        self.s.push(node)
        children = []
        if self.s.is_empty() == False:
          if self.s.peek() not in self.visited:
            self.visited.append(self.s.peek())
            children = self.graph[self.s.peek()]
            if children == []:
              self.s.pop()
            elif children[0] == node1:
              self.visited.append(node1)
              return self.visited
            else:
              self.dfs(children[0], node1)
        return self.visited
    """
    BFS: Push all children of a node into a queue at once and mark them all visited until you find node1
    """
    def bfs(self, node, node1):
        children_temp = self.graph[node]
        children_temp1 = self.graph[node1]
        if node not in self.graph or node1 not in self.graph or children_temp == [] or children_temp1 == []:
          return self.seen
        if node not in self.seen:
          self.seen.append(node)
          children = [child for child in children_temp if child not in self.seen]
          for child in children:
            self.q.push(child)
            if child == node1:
              self.seen.append(child)
              return self.seen
          top = self.q.peek()
          self.q.pop()
          self.bfs(top, node1)
        return self.seen
        

a = Graph()
a.add_edge("A")
a.add_edge("D")
print(a.print_graph())
a.add_edge("B", "A")
print(a.print_graph())
a.add_edge("C", "A")
print(a.print_graph())
print(a.dfs("D", "B"))
print(a.bfs("B", "C"))

