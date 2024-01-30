"""
Description: This program implementsa solution to assert if a vertex u is reachable from a vertex v.
"""

import sys

visited = {}

def reach(adj, x, y):
    #import pdb; pdb.set_trace()
    adjacent = adj[x-1]
    # Mark node as visited
    visited[x] = True
    # Depth First Search.
    for element in adjacent:
        if visited.get(element, False) == False:
            reach(adj, element, y)


        
    

if __name__ == "__main__":
    #import pdb; pdb.set_trace()
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n_vertices, n_edges = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2*n_edges):2], data[1:2*n_edges:2]))
    x, y = data[2*n_edges:]
    adj = [[] for _ in range(n_vertices)]
    # build adjacency list
    for (a, b) in edges:
        adj[a-1].append(b)
        adj[b-1].append(a)
    reach(adj, x, y)
    if visited.get(y, False) == True:
        print(1)
    else:
        print(0)