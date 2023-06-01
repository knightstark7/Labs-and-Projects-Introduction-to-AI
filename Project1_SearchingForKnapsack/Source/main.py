import random
import os
from branch_and_bound import main as algo_branch_and_bound
from genetic import main as algo_genetic
from local_beam import main as algo_local_beam
from brute_force import main as algo_brute_force

def generate_input_file(file_path, n, W, m, min_weight, max_weight, min_value, max_value):
    weights = [random.randint(min_weight, max_weight) for _ in range(n)]
    values = [random.randint(min_value, max_value) for _ in range(n)]
    classes = [random.randint(1, m) for _ in range(n)]
    with open(file_path, "w") as file:
        file.write(f"{W}\n")
        file.write(f"{m}\n")
        file.write(",".join(map(str, weights)) + "\n")
        file.write(",".join(map(str, values)) + "\n")
        file.write(",".join(map(str, classes)) + "\n")

def test_algorithm(algorithm, num_datasets, n, W, m, min_weight, max_weight, min_value, max_value):
    for i in range(1, num_datasets + 1):
        input_folder = "INPUT"
        output_folder = "OUTPUT"
        if not os.path.exists(input_folder):
            os.makedirs(input_folder)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        input_file = os.path.join(input_folder, f"INPUT_{i}.txt")
        generate_input_file(input_file, n, W, m, min_weight, max_weight, min_value, max_value)
        output_file = os.path.join(output_folder, f"OUTPUT_{i}.txt")
        algorithm(input_file, output_file)

# Algorithm 1: brute force searching
# Algorithm 2: branch and bound
# Algorithm 3: local beam search
# Algorithm 4: genetic algorithms
if __name__ == "__main__":
    #algorithm = algo_brute_force
    algorithm = algo_branch_and_bound
    #algorithm = algo_local_beam
    #algorithm = algo_genetic
    num_datasets = 5
    #size
    n = 50
    W = 1000
    #class
    m = 5
    min_weight = 10
    max_weight = 1000
    min_value = 1
    max_value = 1000
    test_algorithm(algorithm, num_datasets, n, W, m, min_weight, max_weight, min_value, max_value)
