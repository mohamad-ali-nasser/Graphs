from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack, Queue  # These may come in handy


# Load world
world = World()

def walts_to_the_bank(world, traversal_path, initial, first=None):
    
    stack = Stack()
    curr_id = 0
    visited = {curr_id: {}}
    curr_room = world.rooms[curr_id]
    # print(curr_room)
    reverse = {'n': 's',
               'e': 'w',
               's': 'n',
               'w': 'e'}
    for direction in curr_room.get_exits():
        visited[curr_room.id][direction] = False
    # print(visited[curr_room.id])

    # iterating through all rooms as unknown
    def unvisited(graph):
        for i in graph:
            if False in graph[i].values():
                return True
        return False

    def find_new_move_room(visited, current_room, curr_id, initial, first):
        room_exits = visited[curr_id]
        # print(f'room_exits: {room_exits}')
        dirs = []
        # if curr_id == 0 and first == None:
        #         print('OK!!!!!!!')
        #         direction = initial
        #         next_room = current_room.get_room_in_direction(direction)
        #         next_room_id = next_room.id
        #         if room_exits[direction] == False and next_room_id not in visited:
        #             first = True
        #             return direction, next_room, next_room_id
             
        for direction in room_exits:
            dirs.append(direction)
        # print(f'dirs 1: {dirs}')
        random.shuffle(dirs)
        # print(f'dirs 2: {dirs}')
        for direction in dirs:
            next_room = current_room.get_room_in_direction(direction)
            next_room_id = next_room.id
            if room_exits[direction] == False and next_room_id not in visited:
                return direction, next_room, next_room_id
        return None, None, None

    def go_back(traversal_path, visited, curr_room, stack, reverse):
        # print("----------------------------------------------------")
        while True:
            next_move = stack.pop()
            # print(f'next_move: {next_move}')
            traversal_path.append(next_move)
            next_room = curr_room.get_room_in_direction(next_move)
            if False in visited[next_room.id].values():
                # print(f'next_room.id: {next_room.id}')
                return next_room.id
            # print(f'next_room: {next_room}')
            curr_room = next_room

    
    # for direction in curr_room.get_exits():
    #     visited[curr_room.id][direction] = False
    #     print(visited)
    while len(visited) < len(world.rooms) and unvisited(visited):
        curr_room = world.rooms[curr_id]
        if curr_room not in visited:
            visited[curr_id] = {}
            for direction in curr_room.get_exits():
                visited[curr_id][direction] = False
        next_move, next_room, next_room_id = find_new_move_room(visited, curr_room, curr_id, initial, first)
        # print(next_room)
        if next_move == None:
            curr_id = go_back(traversal_path, visited, curr_room, stack, reverse)
            continue
        else:
            traversal_path.append(next_move)
            # next_room = curr_room.get_room_in_direction(next_move)
            visited[curr_id][next_move] = next_room_id
            if next_room_id not in visited:
                visited[next_room_id] = {}
                for direction in next_room.get_exits():
                    visited[next_room_id][direction] = False
            visited[next_room_id][reverse[next_move]] = curr_room
            # print(f'This: {visited, visited[next_room_id], visited[next_room_id][reverse[next_move]], [reverse[next_move]]}')
            stack.push(reverse[next_move])
            curr_id = next_room_id
            
    return traversal_path




# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
print(f'current 1{player.current_room}')
print(f'current world.rooms {world.rooms}')
print(f'current world.rooms[0].get_exits {world.rooms[0].get_exits()}')
# print(f'current world.rooms[0].get_exits {world.rooms[0].get_exits()}')

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# traversal_path = ['n', 'n', 's', 's','s','s','n', 'n', 'e', 'e', 'w', 'w','w','w']
# traversal_path = []

# traversal_path = 
traversal_path = []
# print(traverse(world, traversal_path))
# print(traversal_path)
# TRAVERSAL TEST

class maze_solver:
    def __init__(self):
        pass

    def get_neighbors(self, vertex_id, graph):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in graph:
            return graph[vertex_id]
        else:
            return 0
                # path = len(self.dfs(starting_vertex,number, graph))
                # if path in dft_visited_dict.keys():
                #     dft_visited_dict.update({path: (dft_visited_dict[path], number)})

                # else:
                #     dft_visited_dict.update({path: [number] })

    def dft(self, starting_vertex, graph):
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
            neighbors = []
            directions = []
            temp_number = None
            visited_n = []
            while (len(graph) - len(dft_visited_set)) > -100:
                number = s.pop()
                if (temp_number != None) and (number in graph[temp_number]) and (graph[temp_number][number] != True) : #print(f'graph[temp_number][number]: {graph[temp_number][number]}')
                    directions.append(graph[temp_number][number])  # print(f"ADDED: {graph[temp_number][number]}")
                    graph[temp_number].update({number: True}) # print(f"ADDED: {graph[temp_number][number]}, {graph[temp_number]}, {number}. {temp_number} ")
                # if number not in dft_visited_set:
                dft_visited_set.add(number)
                    
                print(niter)
                # print(s.size())
                print(number)

                if number is None:
                    break
                neighbors = self.get_neighbors(number, graph)
                # print(f'Number: {number}')
                # print(f'graph[number]: {graph[number]}')
                # print(f'neighbors: {neighbors}')

                
                niter+=1
                
                # if s.size() == 0 and len(neighbors)==0:
                    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                #     directions.append(graph[temp_number][number])
                checked = 0
                listy = []
                # for n in neighbors:
                    
                #     if n in dft_visited_set: 
                #             print("GGGGG")
                #             listy.append(n)
                            
                    
                #     # if graph[number][n] == True or (temp_number == n and len(neighbors) != 1):
                #     #     continue
                #     # elif graph[n][number] == True and graph[number][n] == True:
                #     #     continue
                #     # if temp_number == n and len(neighbors) != 1:
                #     #     continue
                #     # if graph[n][number]  == True and len(new_neighbors) == 1:
                #     #     continue
                #     if (graph[n][number]  == True) & (graph[number][n] == True):
                #         checked +=1
                 
                # if checked == 4:
                #     break
                visited_n = []
                for n in neighbors:
                    new_neighbors = self.get_neighbors(n, graph)
                    unvisited = True
                    for new in new_neighbors:
                        # print(f'new: {new}')
                        if new not in dft_visited_set:
                            unvisited = False
                        if new_neighbors[new] == False:
                            unvisited = False
                        # if False in new_neighbors.values():
                        #     unvisited = False
                    if graph[number][n] == True or (temp_number == n and len(neighbors) != 1):
                        continue
                    # print(graph[n][number], n, number)
                    # print( graph[number][n], number, n)
                    # if graph[n][number] == True and graph[number][n] == True:
                    #     print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    #     continue
                    
                    elif n not in dft_visited_set and unvisited == False: 
                        # print("GGGGG")
                        listy.append(n)
                        
                        # q = Queue()
                        # q.enqueue(n)
                    else:
                        listy.insert(0,n)
                        checked += 1
                        
                    # if len(neighbors) != checked and len(listy) == 0:
                    #     s.push(n)
                        
                if len(neighbors) == checked:
                    n_visited = []
                    for n in neighbors:
                        
                        # print(f'n: {n}')
                        s.push(n)
                elif len(listy) > 0:
                    n_visited = []
                    for i in listy:
                        # print(f'Pushed: {i}')
                        # print(f'i: {i}')
                        s.push(i)
                        
                # else:
                #     if len(n_visited) = 
                #     s.push(n)
                        
                if s.size() == 0:
                    for n in neighbors:
                        if temp_number == n and len(neighbors) != 1:
                            continue
                        else:
                            s.push(n)
                            n_visited.append(n)
                    
                # for direction in room_exits:
                #     if room_exits[direction] == False and current_room.get_room_in_direction(direction).id not in visited:
                #         return direction
                    # for new_n in new_neighbors:
                    #     if number in graph[new_n]: 
                    #         if graph[new_n][number]  == True:
                    #             checked = True
                    #             continue
                    #         elif checked == True:
                    #             continue
                    #         else:
                    #             s.push(n)
                            
                    # #     elif checked == True:
                    # #         pass
                    # s.push(n)
                                        
                    # new_neighbors = self.get_neighbors(n, graph)
                    # print(f'new_neighbors: {new_neighbors}')
                    # print(f'new_neighbors[number]: {new_neighbors[number]}')
                    
                    
                    # if new_neighbors[number] == True:
                    #     continue
                    
                temp_number = int(number)
                # print(graph)
            # directions.append(graph[number][number])
            # print(len(graph), len(dft_visited_set))
            graph[temp_number].update({number: True})
            return directions
            
            
    def dfs(self, starting_vertex, destination_vertex, graph):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        
        
        # q = Queue()
        # listy = [starting_vertex]
        # q.enqueue(listy)
        # bfs_visited_set = set()
        # graph_2 = []
        # while q.size() > 0:

        #     number = q.dequeue()
        #     # if number[-1] == 0:
        #     #     pass
        #     # else:
        #     #     graph_2.append(graph[number[-1]])
        #     if number[-1] == destination_vertex:
        #         # bfs_visited_set.add(number)
        #         return number
        #     if number[-1] not in bfs_visited_set:
        #         neighbors = self.get_neighbors(number[-1], graph)
        #         bfs_visited_set.add(number[-1])
        #         # print(number[-1])
        #         # print(graph_2)
        #         # print(neighbors)
        #         for n in neighbors:
        #             temp_listy = number.copy()
        #             temp_listy.append(n)
        #             q.enqueue(temp_listy)
                    
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
                neighbors = self.get_neighbors(number[-1], graph)
                bfs_visited_set.add(number[-1])
                # print(number[-1])
                # print(neighbors)
                for n in neighbors:
                    temp_listy = number.copy()
                    temp_listy.append(n)
                    s.push(temp_listy)


    def get_all_social_paths(self, user_id, graph):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  
        visited = self.dft(user_id, graph)

        
        return visited

# ------------------------------------------------------------------------------------------------------------------------------------------

visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

stack = Stack()
curr = 0
visited = {0: {}}
curr_room = world.rooms
reverse = {'n': 's', 'e': 'w',
            's': 'n', 'w': 'e'}

for i in world.rooms:
    visited.update({i: {}})
for i in visited:
    for exits in curr_room[i].get_exits():
        # print(curr_room[i].get_room_in_direction(exits).id)
        n = curr_room[i].get_room_in_direction(exits).id
        # visited[curr_room[i].id][exits] = curr_room[i].get_room_in_direction(exits).id
        visited[curr_room[i].id][n] = exits

        
m = maze_solver()
traversal_path = []
lengthy = [] 
# print(visited)
"""
for i in ['n', 's', 'e', 'w']:
    initial = i
    traversal_path.append(traverse(world, traversal_path, initial))
for n in traversal_path:
    lengthy.append(len(traversal_path))
minimum = min(lengthy)
index_min = lengthy.index(minimum)
traversal_path = traversal_path[index_min]
"""
initial = 'e'
traversal_path = walts_to_the_bank(world, traversal_path, initial)
niter = 0
while len(traversal_path) > 980:
    niter+=1
    traversal_path = []
    
    traversal_path = walts_to_the_bank(world, traversal_path, initial)
    print(f'niter {niter}: {len(traversal_path)}')
print(traversal_path)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")

['e', 'e', 'w', 'w', 'w', 'w', 's', 's', 'e', 'e', 'n', 'n', 'n', 'e', 'e', 'n', 's', 'w', 'w', 'w', 'w', 'n', 's', 'e', 'e', 's', 's', 's', 'w', 'w', 'n', 'n', 'e', 'e', 's', 'n']