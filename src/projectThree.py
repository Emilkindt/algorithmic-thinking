"""
Template for Project 3
Student will implement four functions:

slow_closest_pairs(cluster_list)
fast_closest_pair(cluster_list) - implement fast_helper()
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a list of clusters in the plane
"""

import math
import Cluster



def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function to compute Euclidean distance between two clusters
    in cluster_list with indices idx1 and idx2

    Returns tuple (dist, idx1, idx2) with idx1 < idx2 where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pairs(cluster_list):
    """
    Compute the set of closest pairs of cluster in list of clusters
    using O(n^2) all pairs algorithm

    Returns the set of all tuples of the form (dist, idx1, idx2)
    where the cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.

    """
    results = set([])
    min_dist = float('inf')
    min_dist_idx1 = None
    min_dist_idx2 = None

    elements = len(cluster_list)
    if elements < 2:
        return (min_dist, min_dist_idx1, min_dist_idx2)

    dist = None
    for idx_i in range(elements):
        for idx_j in range(idx_i+1, elements):
            dist = cluster_list[idx_i].distance(cluster_list[idx_j])
            if dist == min_dist:
                temp = (dist, min(idx_i, idx_j), max(idx_i, idx_j))
                results.add(temp)
            elif dist < min_dist:
                min_dist = dist
                min_dist_idx1 = idx_i
                min_dist_idx2 = idx_j

    first_idx = min(min_dist_idx1, min_dist_idx2)
    second_idx = max(min_dist_idx1, min_dist_idx2)
    temp = (min_dist, first_idx, second_idx)
    results.add(temp)
    return results


#def divide(cluster_list,xsort, ysort):
#    """
#    return the median and others
#    :param xsort:
#    :param ysort:
#    """
#
#    numpoints = len(xsort)
#
#    mid = (cluster_list[xsort[-1]].horiz_center() +
#           cluster_list[xsort[0]].horiz_center()) / 2
#    hleft = xsort[:int(numpoints / 2)]
#    hright = xsort[int(numpoints / 2):]
#    vleft = ysort[:len(hleft)]
#    vright = ysort[len(hleft):]
#
#    return mid, hleft, vleft, hright, vright


def fast_closest_pair(cluster_list):
    """
    Compute a closest pair of clusters in cluster_list
    using O(n log(n)) divide and conquer algorithm

    Returns a tuple (distance, idx1, idx2) with idx1 < idx 2 where
    cluster_list[idx1] and cluster_list[idx2]
    have the smallest distance dist of any pair of clusters
    """

    def fast_helper(cluster_list, horiz_order, vert_order):
        """
        Divide and conquer method for computing distance between closest pair of points
        Running time is O(n * log(n))

        horiz_order and vert_order are lists of indices for clusters
        ordered horizontally and vertically

        Returns a tuple (distance, idx1, idx2) with idx1 < idx 2 where
        cluster_list[idx1] and cluster_list[idx2]
        have the smallest distance dist of any pair of clusters

        """

        # base case
        #if len(horiz_order) <= 3:
        #    return slow_closest_pairs(cluster_list[:3]).pop()
        #else:
        #    mid, hleft, vleft, hright, vright = divide(cluster_list,
        #                                               horiz_order, vert_order)
        #
        #    dist0_0, idx0_0, idx1_0 = fast_helper(cluster_list, hleft, vleft)
        #    dist0_1, idx0_1, idx1_1 = fast_helper(cluster_list, hright, vright)
        #
        #    dist, idx0, idx1 = (dist0_0, idx0_0, idx1_0) if dist0_0 < dist0_1 else (dist0_1, idx0_1, idx1_1)
        #
        #    sss=[]
        #    for idx_v in horiz_order:
        #        if abs(cluster_list[idx_v].horiz_center() - mid) < dist:
        #            sss.append(idx_v)
        #    k_in_s = len(sss)
        #    for idx_i in range(k_in_s):
        #        for idx_j in range(k_in_s):
        #            if idx_i != idx_j:
        #                new_dist = cluster_list[sss[idx_i]].distance(cluster_list[sss[idx_j]])
        #                if new_dist < dist:
        #                    dist, idx0, idx1 = (new_dist, sss[idx_i], sss[idx_j])
        #
        #return (dist, idx0, idx1)

        num_horiz = len(horiz_order)
        if num_horiz <= 3:
            return slow_closest_pairs(cluster_list[:num_horiz])
        else:
            mid = int(num_horiz / 2)
            middle = 0.5 * (cluster_list[horiz_order[mid-1]].horiz_center() +
                            cluster_list[horiz_order[mid]].horiz_center())
            horiz_left = horiz_order[0 : mid]
            horiz_right = horiz_order[mid:]
            vert_left = vert_order[0 : mid]
            vert_right = vert_order[mid:]

            dist_left, node_i_left, node_j_left = fast_helper(cluster_list, horiz_left, vert_left)
            dist_right, node_i_right, node_j_right = fast_helper(cluster_list, horiz_left, vert_left)
            dist, node_i, node_j = min((dist_left, node_i_left, node_j_left), (dist_right, node_i_right, node_j_right))

            sss = []
            for idx_v in vert_order:
                if abs(cluster_list[idx_v].horiz_center() - middle) < dist:
                    sss.append(idx_v)
            k_in_s = len(sss)
            for idx_u in range(k_in_s - 1):
                for idx_v in range(idx_u+1, min(u+4, k)):
                    dist, node_i, node_j = min((dist, node_i, node_j), (cluster_list[sss[idx_u]].distance(cluster_list[sss[idx_v]]), sss[idx_u], sss[idx_v]))
            return (dist, node_i, node_j)

    # compute list of indices for the clusters ordered in the horizontal direction
    hcoord_and_index = [(cluster_list[idx].horiz_center(), idx)
                        for idx in range(len(cluster_list))]
    hcoord_and_index.sort()
    horiz_order = [hcoord_and_index[idx][1] for idx in range(len(hcoord_and_index))]

    # compute list of indices for the clusters ordered in vertical direction
    vcoord_and_index = [(cluster_list[idx].vert_center(), idx)
                        for idx in range(len(cluster_list))]
    vcoord_and_index.sort()
    vert_order = [vcoord_and_index[idx][1] for idx in range(len(vcoord_and_index))]

    # compute answer recursively
    answer = fast_helper(cluster_list, horiz_order, vert_order)
    return (answer[0], min(answer[1:]), max(answer[1:]))



def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function mutates cluster_list

    Input: List of clusters, number of clusters
    Output: List of clusters whose length is num_clusters
    """

    return []




def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters

    Input: List of clusters, number of clusters, number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # initialize k-means clusters to be initial clusters with largest populations

    return []
