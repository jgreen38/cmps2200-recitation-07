from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while frontier:
        curr = frontier.pop()
        for neighbor in graph.get(curr, []):
            if neighbor not in result:
                result.add(neighbor)
                frontier.add(neighbor)
    return result





def connected(graph):
    if not graph:
        return True
    start_node = next(iter(graph))
    reachable_nodes = reachable(graph, start_node)
    return len(reachable_nodes) == len(graph)




def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    remaining_nodes = set(graph.keys())
    num_components = 0

    while remaining_nodes:
        start_node = remaining_nodes.pop()
        reachable_nodes = reachable(graph, start_node)
        remaining_nodes -= reachable_nodes
        num_components += 1

    return num_components

