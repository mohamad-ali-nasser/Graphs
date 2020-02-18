"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            print("Vertex_id already exists")
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            return self.vertices[v1].add(v2)
        else:
            raise IndexError("Index does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise IndexError("Index does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        bft_visited_set = set()
        while q.size() > 0:
            number = q.dequeue()
            
            if number not in bft_visited_set:
                bft_visited_set.add(number)

                neighbors = self.get_neighbors(number)
                for n in neighbors:
                    q.enqueue(n)
                
        return bft_visited_set


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        dft_visited_set = set()
        while s.size() > 0:
            number = s.pop()
            
            if number not in dft_visited_set:
                dft_visited_set.add(number)

                neighbors = self.get_neighbors(number)
                for n in neighbors:
                    s.push(n)
                
        return dft_visited_set

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        s = Stack()
        if s.size() == 0:
            print("SMTHG")
            s = Stack()
            dft_visited_set = set()
            s.push(starting_vertex)
            number = s.pop()
        
        
        print(f"number 1: {number}")
        # if number not in dft_visited_set:
        #     dft_visited_set.add(number)
        #     print(f"dft_visited_set 1: {dft_visited_set}")
        #     neighbors = self.get_neighbors(number)
        #     print(f"get_neighbors 1: {neighbors}")
        #     number = s.pop()
        #     for n in neighbors:
        #         dft_visited_set = self.dft_recursive(n)
        #         print(f"dft_visited_set 2: {dft_visited_set}")
        #         print(f"n: {n}")
        #         return dft_visited_set
        
        

        
        # print(f"number 1: {number}")
        # if number not in dft_visited_set:
        #         dft_visited_set.add(number)
        #         print(f"dft_visited_set 1: {dft_visited_set}")
        #         neighbors = self.get_neighbors(number)
        #         print(f"get_neighbors 1: {neighbors}")
        #         for n in neighbors:
        #             dft_recursive(s.push(n).pop())
        #             print(f"dft_visited_set 2: {dft_visited_set}")
        #             print(f"n: {n}")
        
        # s.push(starting_vertex)
        #         # return s.pop()
        # # print(f"dft_visited_set 2: {dft_visited_set}")
        # # dft_visited_set = dft_recursive(self, 1)
        # print(f"dft_visited_set 3: {dft_visited_set}")
        # while s.size() > 0:
        #     number = s.pop()
            
        #     if number not in dft_visited_set:
        #         dft_visited_set.add(number)

        #         neighbors = self.get_neighbors(number)
        #         for n in neighbors:
        #             s.push(n)
                
        # return dft_visited_set

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
                # Create an empty queue
        # Add A PATH TO the starting vertex_id to the queue
        # Create an empty set to store visited nodes
        # While the queue is not empty...
            # Dequeue, the first PATH
            # GRAB THE LAST VERTEX FROM THE PATH
            # CHECK IF IT'S THE TARGET
                # IF SO, RETURN THE PATH
            # Check if it's been visited
            # If it has not been visited...
                # Mark it as visited
                # Then add A PATH TO all neighbors to the back of the queue
                    # (Make a copy of the path before adding)
        q = Queue()
        listy = [starting_vertex]
        q.enqueue(listy)
        bfs_visited_set = set()
        
        while q.size() > 0:
            
            number = q.dequeue()
            if number[-1] == destination_vertex:
                # bfs_visited_set.add(number)
                return number
            if number[-1] not in bfs_visited_set:
                neighbors = self.get_neighbors(number[-1])
                bfs_visited_set.add(number[-1])
                
                for n in neighbors:
                    temp_listy = number.copy()
                    temp_listy.append(n)
                    q.enqueue(temp_listy)
                
        # return bfs_visited_set
        
        # q = Queue()
        # q.enqueue([starting_vertex])
        # bfs_visited_set = set()
        
        # while q.size() > 0:
        #     print(0)
        #     number = q.dequeue()
        #     print(number)
        #     if destination_vertex == number[-1]:
        #         # bfs_visited_set.add(number[-1])
        #         return number
        #     last_number = number[-1]
        #     if last_number not in bfs_visited_set:
        #         bfs_visited_set.add(last_number)
        #         for n in number:
        #             neighbors = self.get_neighbors(n)
                    
        #             temp_list = []
        #             for i in neighbors:
        #                 temp_list.append(i)
        #             q.enqueue(temp_list) 
                

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    print(graph.get_neighbors(2), graph.get_neighbors(5))
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)
    print(graph.bft(1))

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print(graph.dft(1))
    print(graph.dft_recursive(1))

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
