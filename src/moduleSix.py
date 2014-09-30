"""
Solution of application 3
"""

# api
from alg_cluster import Cluster as cls

# solution
from projectThree import slow_closest_pairs as slow
from projectThree import fast_closest_pair as fast
from projectThree import hierarchical_clustering as hierarchical
from projectThree import kmeans_clustering as kmeans

# general
from random import randint as rand
from time import clock as timer
import matplotlib.pyplot as plt


# Question 1
def gen_random_clusters(num_clusters):
    clist = []
    for _dummy_idx in range(num_clusters):
        clist.append(cls(set([]), rand(-1, 1), rand(-1, 1), rand(0, 1), rand(-1, 1)))

    return clist

def simulator():
    res_slow = []
    res_fast = []

    clusters = []
    for size in range(2, 201):
        clusters.append(gen_random_clusters(size))

    # slow
    for clist in clusters:
        slow_start = timer()
        slow(clist)
        slow_end = timer()
        res_slow.append(slow_end - slow_start)

    # fast
    for clist in clusters:
        fast_start = timer()
        fast(clist)
        fast_end = timer()
        res_fast.append(fast_end - fast_start)


    x_axis = [num for num in range(2, 201)]
    plt.title('Comparison of efficiency in desktop python environment')
    plt.xlabel('size of random clusters')
    plt.ylabel('running time (seconds)')
    plt.plot(x_axis, res_slow, '-b', label='slow_closest_pair', linewidth=2)
    plt.plot(x_axis, res_fast, '-r', label='fast_closest_pair', linewidth=2)
    plt.legend(loc='upper left')
    plt.show()


if __name__ == '__main__':
    simulator()
