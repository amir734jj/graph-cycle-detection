from graph import Graph


class DfsGraph(Graph):
    def __init__(self, vertices):
        super().__init__(vertices)

    def is_cyclic_util(self, v, visited, rec_stack):
        """ Recursive utility function to check if there is a cycle """

        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        rec_stack[v] = True

        # Recursive for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.is_cyclic_util(neighbour, visited, rec_stack):
                    return True
            elif rec_stack[neighbour]:
                return True

        # The node needs to be pop-ed from
        # recursion stack before function ends
        rec_stack[v] = False
        return False

    def is_cyclic(self):
        """ The main function to check whether a given graph contains cycle or not """

        visited = [False] * self.V
        rec_stack = [False] * self.V
        for node in range(self.V):
            if not visited[node]:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True
        return False


if __name__ == '__main__':
    g = DfsGraph(3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)

    if g.is_cyclic():
        print("Graph contains cycle")
    else:
        print("Graph does not contain cycle ")
