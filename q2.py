from typing import Callable
from enum import Enum
import doctest


class OutputType(Enum):
    '''
        An Enum class to retrieve one of two options - size of each connected components or a detailed list of each connected components
    '''
    SIZE = 0 #each component size
    CONNECTED_COMPONENTS = 1 #list of all connected components


class Graph:
    '''
        A class represents Graph

        ----------------------------------------------------------------------TESTS----------------------------------------------------------------------
        >>> my_graph = Graph(5)
        >>> my_graph.add_edge(1, 0)
        >>> my_graph.add_edge(2, 3)
        >>> my_graph.add_edge(3, 0)
        >>> print (my_graph.connected_components(my_graph.bfs_Utility, OutputType.CONNECTED_COMPONENTS))
        [[0, 1, 2, 3], [4]]
        >>> print(my_graph.connected_components(my_graph.dfs_utility, OutputType.SIZE))
        [1, 4]
        >>> my_graph.add_edge(0, 4)
        >>> print (my_graph.connected_components(my_graph.bfs_Utility, OutputType.CONNECTED_COMPONENTS))
        [[0, 1, 2, 3, 4]]
        >>> print(my_graph.connected_components(my_graph.dfs_utility, OutputType.SIZE))
        [5]
        
    '''
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def dfs_utility(self, v, visited):
        '''
            Recursive DFS algorithm.
            @param v - a starting vertex
            @param visited - a list of all none-visited vertexes
            Taken from https://www.tutorialspoint.com/python-program-to-find-all-connected-components-using-dfs-in-an-undirected-graph
        '''
        visited[v] = True
        connected_components = [v]
        for i in self.adj[v]:
            if visited[i] == False:
                connected_components.extend(self.dfs_utility(i, visited))
        return connected_components

    def bfs_Utility(self, v, visited):
        '''
            Iterative BFS.
            @param v - a starting vertex
            @param visited - a list of all none-visited vertexes
        '''
        q = [v]
        connected_components = []
        while q:
            current_node = q.pop(0)
            if visited[current_node] == False:
                connected_components.append(current_node)
                visited[current_node] = True
            #if it's neighbors haven't been traversed - add the to the queue
            for i in self.adj[current_node]:
                if not visited[i]:
                    q.append(i)
        return connected_components

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def connected_components(self, algorithm: Callable = dfs_utility, output_type: OutputType = OutputType.SIZE):
        visited = []
        con_component = []
        for _ in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                con_component.append(algorithm(v, visited))
        sum = []
        for component in con_component:
            component.sort()
            sum.append(len(component))
        sum.sort()
        return sum if output_type == OutputType.SIZE else con_component


if __name__ == '__main__':
     doctest.testmod()