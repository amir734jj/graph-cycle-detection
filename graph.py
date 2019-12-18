from collections import defaultdict


class Graph:
    """ This class represents a undirected graph using adjacency list representation """

    def __init__(self, vertices):
        """ Constructor that takes number of nodes in the graph """
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    def add_edge(self, u, v):
        """ function to add an edge to graph """
        self.graph[u].append(v)

    def is_cyclic(self):
        raise Exception("Not implemented")
