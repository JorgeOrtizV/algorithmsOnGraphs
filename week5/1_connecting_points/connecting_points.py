'''
Given 𝑛 points on a plane, connect them with segments of minimum total length such that there is a
path between any two points. Recall that the length of a segment with endpoints (𝑥1, 𝑦1) and (𝑥2, 𝑦2)
is equal to sqrt((𝑥1 − 𝑥2)2 + (𝑦1 − 𝑦2)2)
'''
import sys
import math
from itertools import combinations

# Custom Implementation of priority queue - The existing library doesn't satisfy the requirements
class priorityQueue():
    def __init__(self):
        self.q = dict()
    
    def _put(self, priority, value):
        self.q[value] = priority
    
    def _get(self):
        smallest_priority = min(self.q, key=self.q.get)
        del(self.q[smallest_priority])
        return smallest_priority
    
    def _update(self, priority, value):
        self.q[value] = priority
    
    def _empty(self):
        if len(self.q) == 0:
            return True
        else:
            return False

# class disjoint_sets:
#     def __init__(self, num_sets):
#         self.disjoint_sets = []
#         for i in range(num_sets):
#             single_set = set()
#             single_set.add(i)
#             self.disjoint_sets.append(single_set)

#     def find(self, element):
#         for i in range(len(self.disjoint_sets)):
#             if element in self.disjoint_sets[i]:
#                 return i
            
#     def merge(self, set1, set2):
#         union = self.disjoint_sets[set1].union(self.disjoint_sets[set2])
#         del(self.disjoint_sets[set1])
#         del(self.disjoint_sets[set2])
#         self.disjoint_sets.append(union)

def distance(point1, point2, x, y):
    return math.sqrt(((x[point1]-x[point2])**2)+((y[point1]-y[point2])**2))

# Implementation of Prim's algorithm
def minimum_distance(x, y):
    # Build edge list
    edges = combinations(range(len(x)),2)
    edge_list = []
    for i in list(edges):
        edge_list.append((i[0], i[1], distance(i[0], i[1], x, y)))

    # Initialization
    q = priorityQueue()
    distance_dict = dict()
    parent_dict = dict()
    for i in range(len(x)):
        distance_dict[i]=10e9 # According to constraints weights can't be larger. This is equivalent to infinity
        parent_dict[i]=None
    
    # arbitrary start on node 0
    distance_dict[0] = 0
    # Initial fill up of the priority queue
    for k, v in distance_dict.items():
        q._put(v, k)

    # Prim's algorithm
    visited = set()
    visited.add(0)
    while not q._empty():
        # import pdb; pdb.set_trace()
        u = q._get()
        for a, b, w in edge_list:
            if a == u or b == u:
                not_u = b if a==u else a
                if distance_dict[not_u] > w and not_u not in visited:
                    distance_dict[not_u] = w
                    parent_dict[not_u] = u
                    # Change priority in queue 
                    q._update(distance_dict[not_u], not_u)
        visited.add(u)
    return sum(list(distance_dict.values()))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
