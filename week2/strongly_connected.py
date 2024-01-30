"""
The police department of a city has made all streets one-way. You would like
to check whether it is still possible to drive legally from any intersection to
any other intersection. For this, you construct a directed graph: vertices are
intersections, there is an edge (𝑢, 𝑣) whenever there is a (one-way) street from
𝑢 to 𝑣 in the city. Then, it suffices to check whether all the vertices in the
graph lie in the same strongly connected component.
"""

import sys

sys.setrecursionlimit(200000)

clock = 1

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

def DFS(adj, visited, post):
    global clock
    for element in range(1,len(adj)+1):
        # If we haven't visit that node go for it, skip if done
        if not visited[element-1]:
            explore(adj, element, visited, post)

def SCCs(adj, adj_r, visited, visited_r, post):
    scc = 0
    DFS(adj_r, visited_r, post)
    scc_post = list(enumerate(post, start=1))
    scc_post.sort(key=lambda x:x[1], reverse=True)
    for v, p in scc_post:
        if not visited[v-1]:
            explore(adj, v, visited, post)
            scc+=1
    return scc




if __name__ == "__main__":
    #import pdb; pdb.set_trace()
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n_vertices, n_edges = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2*n_edges):2], data[1:2*n_edges:2]))
    adj = [[] for _ in range(n_vertices)]
    adj_r = [[] for _ in range(n_vertices)]
    # build adjacency list
    for (a, b) in edges:
        adj[a-1].append(b)
        adj_r[b-1].append(a)
    visited = [False]*(int(n_vertices))
    visited_r = [False]*(int(n_vertices))
    post = [0]*(int(n_vertices))
    # Call SCC
    print(SCCs(adj, adj_r, visited, visited_r, post))