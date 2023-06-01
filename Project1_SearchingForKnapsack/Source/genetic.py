import random
class Item:
    def __init__(self, weight, value, item_class):
        self.weight = weight
        self.value = value
        self.item_class = item_class

def read_input_file(file_name):
    with open(file_name, 'r') as file:
        W = float(file.readline())
        m = int(file.readline())
        weights = list(map(float, file.readline().split(',')))
        values = list(map(int, file.readline().split(',')))
        classes = list(map(int, file.readline().split(',')))

    items = [Item(weights[i], values[i], classes[i]) for i in range(len(weights))]
    return W, m, items

def fitness(solution, W, m, items):
    total_weight = 0
    total_value = 0
    class_set = set()
    for i in range(len(solution)):
        if solution[i] == 1:
            total_weight += items[i].weight
            total_value += items[i].value
            class_set.add(items[i].item_class)

    #check if all classes are absent then return 0
    if total_weight > W or len(class_set) < m:
        return -1
    else:
        return total_value
        

def generate_population(population_size, n):
    return [[random.randint(0, 1) for _ in range(n)] for _ in range(population_size)]

def selection(population, W, m, items):
    fitness_values = [(fitness(solution, W, m, items), solution) for solution in population]
    fitness_values.sort(reverse=True, key=lambda x: x[0])

    return [solution for _, solution in fitness_values[:len(population)//2]]

def crossover(parents):
    offspring = []
    for i in range(0, len(parents) - 1, 2):
        crossover_point = random.randint(1, len(parents[i]) - 1)
        offspring.append(parents[i][:crossover_point] + parents[i+1][crossover_point:])
        offspring.append(parents[i+1][:crossover_point] + parents[i][crossover_point:])

    return offspring

def mutation(offspring, mutation_rate):
    for child in offspring:
        for i in range(len(child)):
            if random.random() < mutation_rate:
                child[i] = 1 - child[i]

    return offspring

def main(input_file, output_file, population_size=150, generations=1200, mutation_rate=0.1):
    W, m, items = read_input_file(input_file)
    n = len(items)
    population = generate_population(population_size, n)

    for _ in range(generations):
        parents = selection(population, W, m, items)
        offspring = crossover(parents)
        population = parents + mutation(offspring, mutation_rate)

    best_solution = max(population, key=lambda x: fitness(x, W, m, items))
    best_value = fitness(best_solution, W, m, items)
    with open(output_file, 'w') as file:
        if best_value == -1:
            file.write('No valid subset found')
        else:
            file.write(str(best_value) + '\n')
            file.write(', '.join(map(str, best_solution)) + '\n')


if __name__ == "__main__":
    input_file = "INPUT_2.txt"
    output_file = "OUTPUT_2.txt"
    main(input_file, output_file)