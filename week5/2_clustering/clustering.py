import sys
import math
from sklearn.cluster import KMeans
import numpy as np
from itertools import combinations

class disjoint_sets:
    def __init__(self, num_sets):
        self.disjoint_sets = []
        for i in range(num_sets):
            single_set = set()
            single_set.add(i)
            self.disjoint_sets.append(single_set)

    def find(self, element):
        for i in range(len(self.disjoint_sets)):
            if element in self.disjoint_sets[i]:
                return i
            
    def merge(self, set1, set2):
        union = self.disjoint_sets[set1].union(self.disjoint_sets[set2])
        bigger = set1 if set1>set2 else set2
        smaller = set2 if bigger==set1 else set1
        del(self.disjoint_sets[bigger])
        del(self.disjoint_sets[smaller])
        self.disjoint_sets.append(union)

    def length(self):
        return len(self.disjoint_sets)

def distance(point1, point2, x, y):
    return math.sqrt(((x[point1]-x[point2])**2)+((y[point1]-y[point2])**2))

def clustering(x, y, k):
    # Obtain clusters
    x_np = np.asarray(x)
    y_np = np.asarray(y)
    X = np.concatenate([x_np.reshape([-1,1]), y_np.reshape([-1,1])], axis=1)
    kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
    clusters = kmeans.labels_
    # Build edge list and obtain all distances among points
    edges = combinations(range(len(x)),2)
    edge_list = []
    for i in list(edges):
        edge_list.append((i[0], i[1], distance(i[0], i[1], x, y)))

    # Obtain minimum distance among points in diferent clusters
    min = 10e19
    for j in range(len(edge_list)):
        if clusters[edge_list[j][0]] == clusters[edge_list[j][1]]:
            continue
        if edge_list[j][2] < min:
            min = edge_list[j][2]

    return min

# Implementation of Kruskal's algorithm
# The deal here is to break the algorithm when number of sets in our disjoint sets data structure is equal to k
def clustering_no_sklearn(x,y,k):
    # Build edge list and obtain all distances among points
    edges = combinations(range(len(x)),2)
    edge_list = []
    for i in list(edges):
        edge_list.append((i[0], i[1], distance(i[0], i[1], x, y)))
    #import pdb; pdb.set_trace()
    # Initialize disjoint set
    disj = disjoint_sets(len(x)) # We will have N disjoint sets
    # Order the edge_list by lower weights
    edge_list = sorted(edge_list, key=lambda x : x[2])
    idx = 0
    while disj.length() > k:
        cluster1 = disj.find(edge_list[idx][0])
        cluster2 = disj.find(edge_list[idx][1])
        if cluster1 != cluster2:
            disj.merge(cluster1, cluster2)
        idx += 1
    # Once we have all the clusters we iterate through edge list again and return the first distance we find with different clusters
    for edge in edge_list:
        if disj.find(edge[0]) != disj.find(edge[1]):
            return edge[2]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering_no_sklearn(x, y, k)))
