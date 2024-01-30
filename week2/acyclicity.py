"""
Description: This program asserts if a graph is a Directed Acyclical Graph (G)
"""
import sys

visited = {}

class Node():
    clock = 1
    def __init__(self):
        self.visited = True
        self.previsit = Node.clock
        self.postvisit = None
        Node.clock += 1

    def mark_postvisit(self):
        self.postvisit = Node.clock
        Node.clock += 1


def explore(edges, adj, x):
    # Mark if a node was visited and save it previsit and post visit time
    adjacent = adj[x-1]
    # Mark node as visited
    visited[x] = Node()
    # Depth First Search.
    for element in adjacent:
        if  (x, element) in edges and element not in visited.keys():
            explore(edges, adj, element)
    visited[x].mark_postvisit()
        

def acyclic(edges, adj):
    #import pdb; pdb.set_trace()
    for element in range(1,len(adj)+1):
        # If we haven't visit that node go for it, skip if done
        if element not in visited.keys():
            explore(edges, adj, element)
    # Check that for every (u, v); post(u) > post(v), return 1 otherwise -> Condition that satisfies DAG
    for x,y in edges:
        if visited[y].postvisit > visited[x].postvisit:
            return 1
    return 0

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
    print(acyclic(edges, adj))