import random
from util import Stack, Queue

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.vertices = {}
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()
        
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.friendships:
            return self.friendships[vertex_id]
        else:
            return 0

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        # Create friendships
        # create a list with all possible friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        print(f'possible_friendships: {possible_friendships}')


        # Shuffle the list
        random.shuffle(possible_friendships)
        print("----")
        print(possible_friendships)
        print("----")
        # Grab the first N pairs from the list and create those friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        # avg_friendships = total_friendships / num_users
        # total_friendships = avg_friendships * num_users
        # N = avg_friendships * num_users // 2

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
            # print(f'Number: {number}')
            # for i in self.friendships[number]:

            if number not in dft_visited_set:
                dft_visited_set.add(number)
                path = len(self.dfs(starting_vertex,number))
                if path in dft_visited_dict.keys():
                    dft_visited_dict.update({path: (dft_visited_dict[path], number)})

                else:
                    dft_visited_dict.update({path: number })

                neighbors = self.get_neighbors(number)

                # listy.append(number_neighbors)
                # if neighbors == 0:
                    
                niter+=1
                number_neighbors += len(neighbors)
                for n in neighbors:
                    # print(n)
                    # if number+1 < len(self.friendships) and n in self.friendships[number+1]:
                    #     continue
                    s.push(n)

        # if len(dft_visited_set) == 1:
        #     return -1            
        # else:

        #     ancestor = dft_visited_dict[max(dft_visited_dict)]
        #     if isinstance(ancestor, tuple):
        #         return min([i for i in ancestor])
        #     else:
        #         return ancestor
        return dft_visited_dict
        
        
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        
        
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
        # while s.size() > 0:
            
        #     number = s.pop()
        #     if number[-1] == destination_vertex:
        #         # bfs_visited_set.add(number)
        #         return number
            
        #     if number[-1] not in bfs_visited_set:
        #         neighbors = self.get_neighbors(number[-1])
        #         bfs_visited_set.add(number[-1])
            
        #         for n in neighbors:
        #             temp_listy = number.copy()
        #             temp_listy.append(n)
        #             s.push(temp_listy) 
    
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # for i in self.friendships:
        #     self.add_vertex(i)
        #     print(i)
        # for j in self.vertices:
        #     for k in self.friendships[j]:
        #         self.add_edge(j, k)
        
        # print(self.vertices)
        
        visited = self.dft(user_id)
        
        

        
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.users)
    print(sg.friendships)
    print(sg.get_all_social_paths(1))
    # connections = sg.get_all_social_paths(1)
    # print(connections)
