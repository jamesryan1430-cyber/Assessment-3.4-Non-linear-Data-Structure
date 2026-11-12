"""
Assessment 3.3: Non-linear Data Structure
Builds a binary tree and a graph from your last name,
then shows BFS and DFS traversals for both.
"""
from collections import deque


# ---------------------------------------------------------------
# BINARY TREE
# ---------------------------------------------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(letters):
    """Insert letters level by level, left to right (complete binary tree)."""
    if not letters:
        return None
    root = Node(letters[0])
    queue = deque([root])
    i = 1
    while i < len(letters):
        current = queue.popleft()
        current.left = Node(letters[i])
        queue.append(current.left)
        i += 1
        if i < len(letters):
            current.right = Node(letters[i])
            queue.append(current.right)
            i += 1
    return root


def tree_bfs(root):
    """Level-order traversal (uses a queue)."""
    result, queue = [], deque([root] if root else [])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def preorder(node, out):   # Root -> Left -> Right
    if node:
        out.append(node.value)
        preorder(node.left, out)
        preorder(node.right, out)
    return out


def inorder(node, out):    # Left -> Root -> Right
    if node:
        inorder(node.left, out)
        out.append(node.value)
        inorder(node.right, out)
    return out


def postorder(node, out):  # Left -> Right -> Root
    if node:
        postorder(node.left, out)
        postorder(node.right, out)
        out.append(node.value)
    return out


# ---------------------------------------------------------------
# GRAPH (undirected, adjacency list)
# ---------------------------------------------------------------
def build_graph(letters):
    """
    Vertices = unique letters (in order of appearance).
    Edges   = each letter connected to the next letter in the name.
    Edit `edges` below if your instructor wants different connections.
    """
    graph = {}
    for ch in letters:
        graph.setdefault(ch, [])
    edges = [(letters[i], letters[i + 1]) for i in range(len(letters) - 1)]
    for a, b in edges:
        if a != b:
            if b not in graph[a]:
                graph[a].append(b)
            if a not in graph[b]:
                graph[b].append(a)
    return graph


def graph_bfs(graph, start):
    """Breadth-first search (uses a queue)."""
    visited, order, queue = {start}, [], deque([start])
    while queue:
        v = queue.popleft()
        order.append(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def graph_dfs(graph, start):
    """Depth-first search (recursive, uses the call stack)."""
    visited, order = set(), []

    def visit(v):
        visited.add(v)
        order.append(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return order


# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------
if __name__ == "__main__":
    name = "MARTINEZ"  # change this to use a different last name
    letters = list(name)

    # Tree
    root = build_tree(letters)
    print("\n=== BINARY TREE ===")
    print("Letters (level order):", letters)
    print("BFS (level-order):", " ".join(tree_bfs(root)))
    print("DFS Pre-order    :", " ".join(preorder(root, [])))
    print("DFS In-order     :", " ".join(inorder(root, [])))
    print("DFS Post-order   :", " ".join(postorder(root, [])))

    # Graph
    graph = build_graph(letters)
    print("\n=== GRAPH ===")
    print("Adjacency list:")
    for vertex, neighbors in graph.items():
        print(f"  {vertex}: {neighbors}")
    start = letters[0]
    print(f"BFS from {start}:", " ".join(graph_bfs(graph, start)))
    print(f"DFS from {start}:", " ".join(graph_dfs(graph, start)))