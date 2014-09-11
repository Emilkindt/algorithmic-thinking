#!/usr/bin/env python

"""
Module computes the resilience of given graphs
"""
# Compute the resilience
from projectTwo import compute_resilience
# Choice the attack order
from makeGraphs import random_order
# generate graphs
from makeGraphs import loadOffline
from makeGraphs import erGraph
from makeGraphs import upaGraph
from makeGraphs import upaPlus
# counter
from makeGraphs import counter

import matplotlib.pyplot as plt


network_graph = counter(loadOffline,
                        graph_file="../ref/example_computer_network.txt")
er_graph = counter(erGraph, num_nodes=1347, threshold=0.0017)
upa_graph = counter(upaGraph, all_nodes=1347, existed_nodes=32, num_edges=2)
upa_plus = counter(upaPlus, all_nodes=1347, existed_nodes=2)


def calc(graph):
    order = random_order(graph)
    resilience = compute_resilience(graph, order)
    return resilience


res_network_graph = calc(network_graph)
res_er_graph = calc(er_graph)
res_upa_graph = calc(upa_graph)
res_upa_plus = calc(upa_plus)
removed_nodes = [node for node in range(1348)]

plt.title("Resilience comparison")
plt.xlabel("the number of nodes removed")
plt.ylabel("the largest connect component")
plt.plot(removed_nodes, res_network_graph, '-b', label='Computer network')
plt.plot(removed_nodes, res_er_graph, '-r', label='ER; p=0.0017')
plt.plot(removed_nodes, res_upa_graph, '-g', label='UPA; m=2')
plt.plot(removed_nodes, res_upa_plus, '-y', label="UPA+; m=2")

plt.legend(loc='upper right')
plt.show()
