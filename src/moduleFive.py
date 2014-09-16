#!/usr/bin/env python

from makeGraphs import targeted_order
from makeGraphs import fast_targeted_order
from makeGraphs import upaPlus

import time
import matplotlib.pyplot as plt


def timer(func):
    spent = []

    for num_nodes in range(10, 1000, 10):
        ugraph = upaPlus(num_nodes, 5)

        start = time.clock()
        func(ugraph)
        end = time.clock()

        spent.append(end - start)

    return spent


if __name__ == '__main__':

    slow = timer(targeted_order)
    fast = timer(fast_targeted_order)
    nodes = [node for node in range(10, 1000, 10)]

    plt.plot(nodes, slow, '-b', label='targeted_order', linewidth=2)
    plt.plot(nodes, fast, '-r', label='fast_targeted_order', linewidth=2)

    plt.title("Running time comparison (Implementation of Desktop Python environment)")
    plt.xlabel("the number of nodes")
    plt.ylabel("running times, (seconds)")
    plt.legend(loc='upper left')
    plt.show()
