from typing import List


class FloorPlan:
    # floor plan is a dictionary of Nodes to all of their connected Edges
    def __init__(self):
        self._graph = {}

    class Node:
        def __init__(self, name: str):
            self.name = name

        # types of nodes based on: https://www.researchgate.net/publication/277318124_Generation_of_navigation_graphs_for_indoor_space 
        class Room:
            pass
        class Portal:
            pass
        class Stairwell:
            pass
        class Elevator:
            pass 

    class Edge:
        # connection between two nodes (bidirectional)
        def __init__(self, start_node, end_node, path_cost: int = 1):
            if not isinstance(start_node, FloorPlan.Node) or not isinstance(end_node, FloorPlan.Node):
                raise TypeError('Node type expected')

            self.start_node = start_node
            self.end_node = end_node
            self.path_cost = path_cost

        def __str__(self):
            return "{} -> {}".format(self.start_node, self.end_node)

    def add_node(self, node: Node, edges: List[Edge] = []):
        self._graph[node] = edges

    def add_edges_to_node(self, node: Node, edges: List[Edge]):
        self._graph[node].append(edges)

    def add_edge(self, edge: Edge):
        start_node = edge.start_node
        end_node = edge.end_node
        self.add_edges_to_node(start_node, [edge])
        self.add_edges_to_node(start_node, [edge])