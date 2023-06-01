import heapq
from collections import namedtuple

Item = namedtuple("Item", ["index", "weight", "value", "item_class"])

class Node:
    def __init__(self, level, weight, value, bound, item_set, item_classes):
        self.level = level
        self.weight = weight
        self.value = value
        self.bound = bound
        self.item_set = item_set
        self.item_classes = item_classes

    def __lt__(self, other):
        return self.bound > other.bound

def read_input_file(file_name):
    with open(file_name, 'r') as file:
        W = float(file.readline())
        m = int(file.readline())
        weights = list(map(float, file.readline().split(',')))
        values = list(map(int, file.readline().split(',')))
        classes = list(map(int, file.readline().split(',')))

    items = [Item(i, weights[i], values[i], classes[i]) for i in range(len(weights))]
    return W, m, items

def bound(node, W, items):
    if node.weight >= W:
        return 0

    value_bound = node.value
    weight = node.weight
    level = node.level + 1

    while level < len(items) and weight + items[level].weight <= W:
        weight += items[level].weight
        value_bound += items[level].value
        level += 1

    if level < len(items):
        value_bound += (W - weight) * (items[level].value / items[level].weight)

    return value_bound

def branch_and_bound(W, m, items):
    items.sort(key=lambda x: x.value / x.weight, reverse=True)
    max_value = 0
    best_set = []

    root = Node(-1, 0, 0, 0, [], set())
    root.bound = bound(root, W, items)
    q = []
    heapq.heappush(q, root)

    while q:
        current = heapq.heappop(q)

        if current.bound > max_value and current.level < len(items) - 1:
            level = current.level + 1
            item = items[level]
            # create a child node, with the item from the current node added
            child = Node(level, current.weight + item.weight, current.value + item.value,
                         current.bound, current.item_set + [item.index], current.item_classes | {item.item_class})

            if child.value > max_value and child.weight <= W and len(child.item_classes) == m:
                max_value = child.value
                best_set = child.item_set

            child.bound = bound(child, W, items)
            if child.bound > max_value:
                heapq.heappush(q, child)
            # create a child node, without the item from the current node
            child = Node(level, current.weight, current.value, current.bound, current.item_set, current.item_classes)
            child.bound = bound(child, W, items)
            if child.bound > max_value:
                heapq.heappush(q, child)

    return max_value, best_set

def main(input_file, output_file):
    W, m, items = read_input_file(input_file)
    max_value, best_set = branch_and_bound(W, m, items)
    with open(output_file, 'w') as file:
        if max_value == 0: 
            file.write("No valid subset found")
        else:
            solution = [0] * len(items)
            for _ in best_set:
                solution[_] = 1
            file.write(f"{max_value}\n")
            file.write(', '.join(map(str, solution)) + '\n')
if __name__ == "__main__":
    input_file = "INPUT_2.txt"
    output_file = "OUTPUT_2.txt"
    main(input_file, output_file)