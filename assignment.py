from __future__ import annotations

import networkx as nx


def max_weighted_clique(graph: nx.Graph) -> tuple:
    """Finds a maximum-weight clique in a graph with non-negative vertex weights.

    Note: We are interested in the clique with maximum total weight.
    This is not necessarily the same as the clique with the maximum number of vertices.

    :param graph: A NetworkX Graph where vertices have a "weight" attribute.
    :return clique: A list or tuple of vertices constituting a largest vertex weighted clique in the graph.
    """

    # TODO
    pass


def longest_path(graph: nx.Graph) -> tuple:
    """Finds a longest simple path in a graph with non-negative edge weights.

    :param graph: A NetworkX Graph where edges have a "weight" attribute.
    :return path: A list or tuple of vertices constituting a longest path in the graph.
    """

    # TODO
    pass


def knapsack_01(capacity: float, values: list[float], weights: list[float]) -> tuple[int]:
    """Maximize the value in the knapsack given the item values and capacity constraint.

    Note: We are interested in solving the 0-1 knapsack problem where the capacity and weights are not restricted to integer values.

    :param capacity: The capacity of the knapsack.
    :param values: The values for each item.
    :param weights: The weights for each item.
    :return items: A list or tuple of integers specifying the item numbers/indices making the best value knapsack given the capacity constraints.
    """
    assert len(weights) == len(values)

    # TODO
    pass

