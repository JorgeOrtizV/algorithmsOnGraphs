"""
Description: This program asserts if a graph is a Directed Acyclical Graph (G)
"""
import sys

clock = 1

"""
Comments:
    1. I do not store previsit, since it is not relevant for topological sort
    2. Modified Adjacency list, since it is a Directed list, only (a,b) is relevant (because direction), so in adjacency list we just add adj(a).append(b)
            This also serve as a direction check
            Remember for undirected graphs we also add adj(b).append(a), but doing this doubles the amount of operations and it is unnecesary. Additionally a 
            direction check would be necessary.
"""

def explore(adj, x, visited, post):
    global clock
    # Mark if a node was visited and save it previsit and post visit time
    adjacent = adj[x-1]
    # Mark node as visited
    visited[x-1] = True
    # Depth First Search.
    for element in adjacent:
        if  not visited[element-1]:
            explore(adj, element, visited, post)
    post[x-1] = clock
    clock +=1
        

def topsort(adj, visited, post):
    global clock
    #import pdb; pdb.set_trace()
    for element in range(1,len(adj)+1):
        # If we haven't visit that node go for it, skip if done
        if not visited[element-1]:
            explore(adj, element, visited, post)
    # Sort according postorder in increasing order
    post = list(enumerate(post, start=1))
    post.sort(key=lambda x:x[1], reverse=True)
    return post

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
    visited = [False]*(int(n_vertices))
    post = [0]*(int(n_vertices))
    postorder = topsort(adj, visited, post)
    for v, post in postorder:
        print(v, end=' ')