import math

class Node:
    def __init__(self, name, is_terminal=False, value=None):
        self.name = name
        self.is_terminal = is_terminal
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def minimax(node, depth, is_maximizing):
    if depth == 0 or node.is_terminal:
        return node.value

    if is_maximizing:
        max_eval = -math.inf
        for child in node.children:
            eval_val = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval_val)
        node.value = max_eval
        return max_eval
    else:
        min_eval = math.inf
        for child in node.children:
            eval_val = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval_val)
        node.value = min_eval
        return min_eval

def print_tree(node, prefix="", is_last=True):
    marker = "└── " if is_last else "├── "
    print(f"{prefix}{marker}{node.name} (Value: {node.value})")
    prefix += "    " if is_last else "│   "
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        print_tree(child, prefix, i == child_count - 1)

leaf_values = [3, 5, 2, 9, 12, 0, -4, 6]
leaves = [Node(f"L4_{i+1}", is_terminal=True, value=v) for i, v in enumerate(leaf_values)]

l3_nodes = [Node(f"L3_{chr(65+i)}") for i in range(4)]
for i, node in enumerate(l3_nodes):
    node.add_child(leaves[i * 2])
    node.add_child(leaves[i * 2 + 1])

l2_Left, l2_Right = Node("L2_Left"), Node("L2_Right")
l2_Left.add_child(l3_nodes[0])
l2_Left.add_child(l3_nodes[1])
l2_Right.add_child(l3_nodes[2])
l2_Right.add_child(l3_nodes[3])

root = Node("Root_MAX")
root.add_child(l2_Left)
root.add_child(l2_Right)

best_score = minimax(root, depth=3, is_maximizing=True)
print("\n--- Evaluated Game Tree ---")
print_tree(root)
print("-" * 28)
print(f"Best Score at Root Node: {best_score}")
