import random

def local_beam_search(W, m, weights, values, classes, k=10, max_iterations=100):
    n = len(weights)

    def generate_initial_states():
        states = []
        for i in range(k):
            state = []
            for j in range(n):
                if random.random() < 0.5:
                    state.append(1)
                else:
                    state.append(0)
            states.append(state)
        return states

    def evaluate(state):
        total_weight = 0
        total_value = 0
        class_items = {i: False for i in range(1, m + 1)}
        for i in range(n):
            if state[i] == 1:
                total_weight += weights[i]
                total_value += values[i]
                class_items[classes[i]] = True
        if total_weight > W or False in class_items.values():
            return 0
        else:
            return total_value

    def get_neighbors(state):
        neighbors = []
        for i in range(n):
            neighbor = state.copy()
            neighbor[i] = 1 - neighbor[i]
            neighbors.append(neighbor)
        return neighbors

    current_states = generate_initial_states()
    best_state = max(current_states, key=evaluate)
    best_value = evaluate(best_state)
    iterations = 0
    while iterations < max_iterations:
        iterations += 1
        next_states = []
        for state in current_states:
            next_states.extend(get_neighbors(state))
        next_states = sorted(next_states, key=evaluate, reverse=True)[:k]
        current_states = next_states
        current_best_state = max(current_states, key=evaluate)
        current_best_value = evaluate(current_best_state)
        if current_best_value > best_value:
            best_state = current_best_state
            best_value = current_best_value
    return best_value, best_state


def read_input_file(file_path):
    with open(file_path, 'r') as f:
        W = float(f.readline().strip())
        m = int(f.readline().strip())
        wi = list(map(float, f.readline().strip().split(',')))
        vi = list(map(int, f.readline().strip().split(',')))
        ci = list(map(int, f.readline().strip().split(',')))
    return W, m, wi, vi, ci

def write_output_file(file_path, max_value, items_in_knapsack):
    with open(file_path, 'w') as f:
        if (max_value == 0):
            f.write('No valid subset found')
        else:
            f.write(str(max_value) + '\n')
            f.write(', '.join(map(str, items_in_knapsack)))

def main(input_file, output_file):
    W, m, weights, values, class_labels = read_input_file(input_file)
    # set algorithm parameters
    k = 200 # number of beams
    max_iterations = 1200
    # run local beam search algorithm
    best_value, best_items = local_beam_search(W, m, weights, values, class_labels, k, max_iterations)
    write_output_file(output_file, best_value, best_items)


if __name__ == '__main__':
    input_file = "INPUT_2.txt"
    output_file = "OUTPUT_2.txt"
    main(input_file, output_file)


