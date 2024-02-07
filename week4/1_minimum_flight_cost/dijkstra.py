'''
Now, you are interested in minimizing not the number of segments, but the total cost of a flight. For this
you construct a weighted graph: the weight of an edge from one city to another one is the cost of the
corresponding flight.

Given an directed graph with positive edge weights and with 𝑛 vertices and 𝑚 edges as well as two
vertices 𝑢 and 𝑣, compute the weight of a shortest path between 𝑢 and 𝑣 (that is, the minimum total
weight of a path from 𝑢 to 𝑣)
'''

import sys
import queue

# Custom Implementation of priority queue - The existing library doesn't satisfy the requirements
class priorityQueue():
    def __init__(self):
        self.q = dict()
    
    def _put(self, priority, value):
        self.q[value] = priority
    
    def _get(self):
        smallest_priority = min(self.q, key=self.q.get)
        del(self.q[smallest_priority])
        return smallest_priority
    
    def _update(self, priority, value):
        self.q[value] = priority
    
    def _empty(self):
        if len(self.q) == 0:
            return True
        else:
            return False

# Implementation of Dijkstra's algorithm
def distance(adj, cost, s, t):
    '''
    Input:
        adj -> adjacency list
        cost -> weights list
        s -> start node
        t -> End node
    '''
    q = priorityQueue()
    vertices = len(adj)
    distance_dict = dict()
    parent_dict = dict()
    for i in range(vertices):
        distance_dict[i]=10e9 # According to constraints weights can't be larger. This is equivalent to infinity
        parent_dict[i]=None
    # We start at node s
    distance_dict[s] = 0
    # Initial fill up of the priority queue
    for k, v in distance_dict.items():
        q._put(v, k)
    while not q._empty():
        # Obtain the lowest priority. According to documentation:
        # The lowest valued entries are retrieved first (the lowest valued entry is the one that would be returned by min(entries)). A typical pattern for entries is a tuple in the form: (priority_number, data).
        u = q._get()
        
        for i, v in enumerate(adj[u]):
            if distance_dict[v] > distance_dict[u] + cost[u][i]:
                distance_dict[v] = distance_dict[u] + cost[u][i]
                parent_dict[v] = u
                # Change priority in queue 
                q._update(distance_dict[v], v)
        
    # There is a smaller distance than initialization, therefore s->t is possible, otherwise we return -1
    if distance_dict[t] < 10e9:
        return distance_dict[t]
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
