def loadGraph(originalData):
    data_lines = []
    digraph = {}
    
    with open(originalData) as f:
        for line in f.readlines():
            data_lines.append(line[ : -1])

    for line in data_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        digraph[node] = set()
        for edge in neighbors[1 : -1]:
            digraph[node].add(int(edge))

    return digraph


def compute_in_degrees(digraph):
    res = {}
    for n in digraph.keys():
        res[n] = 0
    for v in digraph.values():
        for vv in v:
            res[vv] = 0

    for v in digraph.values():
        for vv in v:
            res[vv] += 1

    return res


def in_degree_distribution(digraph):
    digraph = compute_in_degrees(digraph)
    distribution = {}
    count = 0
    for indegree in digraph.values():
        count += 1
        if indegree not in distribution.keys():
            distribution[indegree] = 0
        distribution[indegree] += 1

    for n in distribution.keys():
        distribution[n] = float(distribution[n]) / float(count)

    return distribution


def calc(filename):
    digraph = loadGraph(filename)
    distribution = in_degree_distribution(digraph)
    distribution.pop(0)
    return distribution

if __name__ == "__main__":
    import scipy
    import matplotlib.pyplot as plt
    dis = calc("alg_phys-cite.txt")
    x = []
    y = []
    for k, v in dis.items():
        x.append(k)
        y.append(v)
    x = scipy.array(x)
    y = scipy.array(y)


    plt.title("citation relationship")
    plt.xlabel("cited, based on 1")
    plt.ylabel("normalized distribution")
    plt.loglog(x, y, 'ro')
    plt.show()

