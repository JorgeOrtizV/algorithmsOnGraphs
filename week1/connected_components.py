"""
Description: This program implements a solution to count the number of connected components in a given graph G.
"""

import sys

visited = {}

def explore(adj, x):
    #import pdb; pdb.set_trace()
    adjacent = adj[x-1]
    # Mark node as visited
    visited[x] = True
    # Depth First Search.
    for element in adjacent:
        if visited.get(element, False) == False:
            explore(adj, element)

def DFS(vertices, adj):
    #import pdb; pdb.set_trace()
    cc = 0
    for element in vertices:
        if visited.get(element, False) == False:
            explore(adj, element) 
            cc += 1
    return cc

if __name__ == "__main__":
    #import pdb; pdb.set_trace()
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n_vertices, n_edges = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2*n_edges):2], data[1:2*n_edges:2]))
    adj = [[] for _ in range(n_vertices)]
    # build adjacency list
    for (a, b) in edges:
        adj[a-1].append(b)
        adj[b-1].append(a)
    num_connected_components = DFS(list(range(1,n_vertices+1)), adj)
    print(num_connected_components)
