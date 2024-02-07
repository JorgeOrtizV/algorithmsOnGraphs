'''
Given an directed graph with possibly negative edge weights and with 𝑛 vertices and 𝑚 edges, check
whether it contains a cycle of negative weight.

Implementation of an algorithm to check for negative cycles in a directed graph
'''

import sys


def bellman_ford(adj, cost, iterations):
    vertices = len(adj)
    distance_dict = dict()
    parent_dict = dict()
    for i in range(vertices):
        distance_dict[i] = 10e9
        parent_dict[i] = None
    # Start at S = 0
    distance_dict[0] = 0
    for it in range(iterations):
        for u in range(vertices):
            for i, v in enumerate(adj[u]):
                if distance_dict[v] > distance_dict[u] + cost[u][i]:
                    distance_dict[v] = distance_dict[u] + cost[u][i]
                    parent_dict[v] = u
    return distance_dict


def negative_cycle(adj, cost):
    #Call bellman-ford v-1 times
    distance_dict = bellman_ford(adj, cost, len(adj)-1)
    # Run Bellman Ford an extra time to see if there is an update
    for u in range(len(adj)):
        for i, v in enumerate(adj[u]):
            if distance_dict[v] > distance_dict[u] + cost[u][i]:
                # We found a negative cycle, therefore we return.
                return 1
    return 0


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
    print(negative_cycle(adj, cost))
