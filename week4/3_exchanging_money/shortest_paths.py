'''
Given an directed graph with possibly negative edge weights and with 𝑛 vertices and 𝑚 edges as well
as its vertex 𝑠, compute the length of shortest paths from 𝑠 to all other vertices of the graph.

Implementation of Bellman Ford Algorithm to obtain shortest paths with negative weights
'''

import sys
import queue

visited = []

# TODO : Needs work, stucked at case 19/36

def bellman_ford(adj, cost, iterations, s):
    global visited
    vertices = len(adj)
    distance_dict = dict()
    parent_dict = dict()
    updated = []
    for i in range(vertices):
        distance_dict[i] = float('inf')
        parent_dict[i] = None
    # Start at S = s
    distance_dict[s] = 0
    for it in range(iterations):
        for u in range(vertices):
            for i, v in enumerate(adj[u]):
                if visited[u] == False or visited[v] == False:
                    continue
                if distance_dict[v] > distance_dict[u] + cost[u][i]:
                    if it >= vertices-2 and v not in updated:
                        updated.append(v)
                    else:
                        distance_dict[v] = distance_dict[u] + cost[u][i]
                        parent_dict[v] = u
    return distance_dict, updated

def DFS(adj, x):
    # Mark node as visited
    visited[x] = True
    # Depth First Search.
    for element in adj[x]:
        if visited[element] == False:
            DFS(adj, element)

def BFS(adj, s):
    vertices = len(adj)
    distance_dict = dict()
    q = queue.Queue()
    affected = []
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
                affected.append(v)
    return affected

def shortest_paths(adj, cost, s):
    # Discover reachable nodes from s
    global visited
    visited = [False]*len(adj)
    DFS(adj, s)
    #Call bellman-ford
    vertices = len(adj)
    distance_dict, updated = bellman_ford(adj, cost, vertices, s)
    
    for i in updated:
        distance_dict[i] = '-'
        # Discover all nodes affected by the negative cycle - BFS
        affected = BFS(adj, i)
        for j in affected:
            distance_dict[j] = '-'
    for idx, val in enumerate(visited):
        if val == False:
            distance_dict[idx] = '*'
    return distance_dict



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
    s = data[0]
    s -= 1
    # distance = [10**19] * n
    # reachable = [0] * n
    # shortest = [1] * n
    distance = shortest_paths(adj, cost, s)
    for x in range(len(distance)):
        if distance[x] == float('inf'):
            distance[x] = '*'
        print(distance[x])

