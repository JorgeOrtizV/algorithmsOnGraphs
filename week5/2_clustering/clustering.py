import sys
import math
from sklearn.cluster import KMeans
import numpy as np
from itertools import combinations

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


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
