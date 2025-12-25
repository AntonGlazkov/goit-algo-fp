import uuid
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def collect_nodes(root):
    nodes = {}
    stack = [root]
    while stack:
        node = stack.pop()
        if node and node.id not in nodes:
            nodes[node.id] = node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return list(nodes.values())


def gradient_colors(n):
    start = (20, 30, 60)     # темний
    end = (200, 220, 255)    # світлий
    colors = []
    for i in range(n):
        r = int(start[0] + (end[0] - start[0]) * i / max(1, n - 1))
        g = int(start[1] + (end[1] - start[1]) * i / max(1, n - 1))
        b = int(start[2] + (end[2] - start[2]) * i / max(1, n - 1))
        colors.append(f"#{r:02X}{g:02X}{b:02X}")
    return colors


def dfs_order(root):
    order = []
    stack = [root]
    visited = set()

    while stack:
        node = stack.pop()
        if node and node.id not in visited:
            visited.add(node.id)
            order.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return order


def bfs_order(root):
    order = []
    q = deque([root])
    visited = set()

    while q:
        node = q.popleft()
        if node and node.id not in visited:
            visited.add(node.id)
            order.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return order


def visualize_traversal(root, order_func):
    nodes = collect_nodes(root)
    colors = gradient_colors(len(nodes))

    order = order_func(root)

    for i, node in enumerate(order):
        node.color = colors[i]
        draw_tree(root)


# Створення дерева 
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

print("DFS visualization")
visualize_traversal(root, dfs_order)

# Повертаємо кольори до базових перед BFS
for n in collect_nodes(root):
    n.color = "#1296F0"

print("BFS visualization")
visualize_traversal(root, bfs_order)
