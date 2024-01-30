'''
You would like to compute the minimum number of flight segments to get from one city to another one. For
this, you construct the following undirected graph: vertices represent cities, there is an edge between two
vertices whenever there is a flight between the corresponding two cities. Then, it suffices to find a shortest
path from one of the given cities to the other one.

Given an undirected graph with 𝑛 vertices and 𝑚 edges and two vertices 𝑢 and 𝑣, compute the length
of a shortest path between 𝑢 and 𝑣 (that is, the minimum number of edges in a path from 𝑢 to 𝑣).
'''

import sys
import queue

# BFS implementation
def distance(adj, s, t):
    vertices = len(adj)
    distance_dict = dict()
    q = queue.Queue()
    for i in range(vertices):
        distance_dict[i] = None
    distance_dict[s] = 0
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in adj[u]:
            if distance_dict[v] == None:
                q.put(v)
                distance_dict[v] = distance_dict[u]+1
                if v == t:
                    # If the node is the same we break and return the obtained distance, since it is not possible
                    # to arrive in a shorter distance. Note we started from the requested start node
                    return distance_dict[v]
    # There is not possible path between s and t
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
