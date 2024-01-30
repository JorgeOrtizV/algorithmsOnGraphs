'''
An undirected graph is called bipartite if its vertices can be split into two parts such that each edge of the
graph joins to vertices from different parts. Bipartite graphs arise naturally in applications where a graph
is used to model connections between objects of two different types (say, boys and girls; or students and
dormitories).
An alternative definition is the following: a graph is bipartite if its vertices can be colored with two colors
(say, black and white) such that the endpoints of each edge have different colors.

Given an undirected graph with 𝑛 vertices and 𝑚 edges, check whether it is bipartite.
'''

import sys
import queue

def bipartite(adj):
    vertices = len(adj)
    group_dict = dict()
    q = queue.Queue()
    for i in range(vertices):
        group_dict[i] = None
    # Since the graph may have many strongly connected components we implemented this naive for loop to discover all the nodes not
    # initially discovered by the BFS of node 0. A better approach would be first to call DFS to get the Strongly Connected elements
    # and then run BFS until no elements are left. 
    for i in range(vertices):
        if group_dict[i] != None:
            continue
        group_dict[i] = 1
        q.put(i)
        while not q.empty():
            u = q.get()
            for v in adj[u]:
                if group_dict[v] == None:
                    q.put(v)
                    group_dict[v] = group_dict[u]*-1
                else:
                    if group_dict[v] != group_dict[u]*-1:
                        return 0
    # There is not possible path between s and t
    return 1

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
    print(bipartite(adj))
