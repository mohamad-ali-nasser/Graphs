# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4


class Graph:
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
        # else:
        #     raise IndexError("Index does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise IndexError("Index does not exist")
        
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        dft_visited_dict = dict()
        dft_visited_set = set()
        niter = 0
        number_neighbors = 0
        while s.size() > 0:
            number = s.pop()
            print(f'Number: {number}')
            if number not in dft_visited_set:
                dft_visited_set.add(number)
                path = len(self.dfs(starting_vertex,number))
                if path in dft_visited_dict.keys():
                    dft_visited_dict.update({path: (dft_visited_dict[path], number)})
                    neighbors = self.get_neighbors(number)

                    niter+=1
                    number_neighbors += len(neighbors)
                    for n in neighbors:
                        s.push(n)
                else:
                    dft_visited_dict.update({path: number })

                    neighbors = self.get_neighbors(number)

                    # listy.append(number_neighbors)
                    niter+=1
                    number_neighbors += len(neighbors)
                    for n in neighbors:
                        s.push(n)
                
        if len(dft_visited_set) == 1:
            return -1            
        else:

            ancestor = dft_visited_dict[max(dft_visited_dict)]
            if isinstance(ancestor, tuple):
                return min([i for i in ancestor])
            else:
                return ancestor
        
        
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        
        s = Stack()
        listy = [starting_vertex]
        s.push(listy)
        bfs_visited_set = set()
        
        while s.size() > 0:
            
            number = s.pop()
            if number[-1] == destination_vertex:
                # bfs_visited_set.add(number)
                return number
            
            if number[-1] not in bfs_visited_set:
                neighbors = self.get_neighbors(number[-1])
                bfs_visited_set.add(number[-1])
            
                for n in neighbors:
                    temp_listy = number.copy()
                    temp_listy.append(n)
                    s.push(temp_listy)

def earliest_ancestor(islands):
    g = Graph()
    for i in islands:
        g.add_vertex(i[0])
        g.add_vertex(i[1])
    
    for i in ancestors:
        g.add_edge(i[1], i[0])
    #     print(f'Ok for {i}')
        
    # print(g.vertices)
    print(g.dft(input)) 
    return g.dft(input)

# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4

for i, j in enumerate(islands):
    print(i,j)