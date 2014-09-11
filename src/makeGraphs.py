#!/usr/bin/env python

"""
This module is used to computes a undirected graph by several methods
includes:
    loadOnline/Offline - load the text representation as an undirected graph
    erGraph - generate an undirected graph by random probability
    upaGraph - iteration to generate a random undirected graph
"""
# when use lodeOnline
# import urllib2

import random
from UPATrial import UPATrial as upa


############
# scaffolds

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph


def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)


def random_order(ugraph):
    """
    Choice a random attack order

    Returns:
    A list of nodes
    """
    new_graph = copy_graph(ugraph)
    nodes = [node for node in new_graph.keys()]
    order = []

    while len(nodes) > 0:
        random_node = random.choice(nodes)
        order.append(random_node)
        delete_node(new_graph, random_node)
        nodes.remove(random_node)

    return order


def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting of
    nodes of maximal degree

    Returns:
    A list of nodes
    """
    new_graph = copy_graph(ugraph)
    order = []

    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node

        delete_node(new_graph, max_degree_node)
        order.append(max_degree_node)

    return order


def counter(func, **kw):
    """
    Function that counts the number of nodes and edges
    """
    graph = func(**kw)
    name = func.__name__
    count_nodes = 0
    count_edges = 0

    for node in graph:
        count_nodes += 1
        count_edges += len(graph[node])

    print("undirected graph {0} has {1} nodes and {2} edges".format(
            name, count_nodes, count_edges / 2.0))
    return graph


def loadOnline(graph_url):
    """
    Function that loads a graph given the URL for a text representation
    of the graph

    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]

    ugraph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        ugraph[node] = set()
        for neighbor in neighbors[1 : -1]:
            ugraph[node].add(int(neighbor))

    return ugraph


def loadOffline(graph_file):
    """
    Offline version of the function loadOnline.
    """
    ugraph = {}

    with open(graph_file) as graph:
        for line in graph.readlines():
            line = line[ : -1]
            neighbors = line.split(' ')
            node = int(neighbors[0])
            ugraph[node] = set()
            for neighbor in neighbors[1 : -1]:
                ugraph[node].add(int(neighbor))

    return ugraph


def erGraph(num_nodes, threshold=1):
    """
    Algorithm ER implementation.

    Input:
        the number of nodes
        probability threshold
    Output:
        a undirected graph
    """
    nodes = {node for node in range(num_nodes)}
    ugraph = {node: set() for node in nodes}

    for node_i in nodes:
        for node_j in nodes:
            if node_i != node_j:
                probability = random.random()
                if probability < threshold:
                    ugraph[node_i].add(node_j)
                    ugraph[node_j].add(node_i)
    return ugraph


def upaGraph(all_nodes, existed_nodes, num_edges):
    """
    Variant implementation of algorithm DPA
    iteration to generate a random undirected graph
    """
    ugraph = erGraph(existed_nodes, 1)
    random_connect = upa(existed_nodes)

    for new_node in range(existed_nodes, all_nodes):
        new_edges = random_connect.run_trial(num_edges)
        ugraph[new_node] = new_edges
        for old_node in new_edges:
            ugraph[old_node].add(new_node)

    return ugraph

def upaPlus(all_nodes, existed_nodes):
    ugraph = erGraph(existed_nodes, 1)
    random_connect = upa(existed_nodes)

    for new_node in range(existed_nodes, all_nodes):
        new_edges = random_connect.run_trial(existed_nodes)
        ugraph[new_node] = new_edges
        for old_node in new_edges:
            ugraph[old_node].add(new_node)
    return ugraph
