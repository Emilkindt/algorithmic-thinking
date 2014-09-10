#!/usr/bin/env python

from random import choice

def bfsDistance(graph, vi):
    pass


def ccDistance(graph):
    """
    Function computes the connected components of a graph
    based on module bfsDistance.

    Input:
    graph = dict(nodes=edges)
    graph = [n0, e1, e2, n1, e0, e2, n2, e0, e1]

    Output:
    the set of connected components
    """

    if isinstance(graph, dict):
        nodes = {n for n in graph.keys()}
    elif isinstance(graph, list):
        nodes = set(graph)
    else:
        raise TypeError

    components = set()

    while nodes != None:
        vi = choice(nodes)
        distance = bfsDistance(graph, vi)
        nodeStore = set()
        for vj in nodes:
            if d[vj] != None:
                nodeStore.add(vj)
        components.update(nodeStore)
        nodes -= nodeStore
    return components


if __name__ == '__main__':
    print("Is working in...")
