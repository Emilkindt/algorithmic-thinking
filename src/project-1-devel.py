#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module is used to represent directed graphs,
and computing degree distributions.
"""

EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3]),
             3: set([0]), 4: set([1]), 5: set([2]), 6: set([])}
EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]),
             3: set([7]), 4: set([1]), 5: set([2]), 6: set([]),
             7: set([3]), 8: set([1, 2]), 9: set([0, 3, 4, 5, 6, 7])}


def make_complete_graph(num_nodes=0):
    """
    This function takes the number of nodes and returns
    a dictionary corresponding to a complete directed graph.
    Contains the specified number of nodes, and all possible edges.
    Input:
        num_nodes = non-negative integer
    Output:
        digraph = {node: {possible edges}, ...}
    """
    try:
        num_nodes = int(float(num_nodes))
    except ValueError:
        num_nodes = 0
    except TypeError:
        num_nodes = 0

    if num_nodes > 0:
        digraph = {}
        nodes = [n for n in range(num_nodes)]
        for node in range(num_nodes):
            digraph[node] = set()
            for edge in nodes:
                if edge != node:
                    digraph[node].add(edge)
        return digraph
    else:
        return {}


def compute_in_degrees(digraph):
    """
    This function takes the directed graph that represented as a dictionary.
    And Returns the graph with in-degrees for the nodes in the graph.
    Input:
        digraph = {node: set([edges]), ...}
    Output:
        digraph = {node: the nubmer of edges, ...}
    """
    # 貌似 codeskulptor 的编译器不允许这种写法?
    # res = {node: 0 for node in digraph.keys()}
    res = {}
    for node in digraph.keys():
        res[node] = 0
    for odegree, idegress in digraph.items():
        for idegree in idegress:
            if idegree not in res.keys():
                res[idegree] = 1
            res[idegree] += 1
    return res


def in_degree_distribution(digraph):
    """
    This function takes the directed graph that represented as a dictionary.
    And Returns the unnormalized distribution of the in-degrees of the graph.
    Input:
        digraph = {node: set([in-degree]), ...}
    Output:
        digraph = {in-degree: number of nodes}
    """
    pass


if __name__ == '__main__':
    import sys

    if sys.argv[1] == "-m":
        print("Test function make_complete_graph():")
        print(make_complete_graph())
        print(make_complete_graph({}))
        print(make_complete_graph("A"))
        print(make_complete_graph("5.5"))
        print(make_complete_graph(10.10))

    if sys.argv[1] == "-c":
        print("Test function compute_in_degrees():")
        print(compute_in_degrees({}))
        print(compute_in_degrees(EX_GRAPH0))
        print(compute_in_degrees(EX_GRAPH1))
        print(compute_in_degrees(EX_GRAPH2))
