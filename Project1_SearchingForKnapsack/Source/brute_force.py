def knapsack_brute_force_searching(capacity, m, weights, values, class_labels):
    """
    Tìm giá trị lớn nhất có thể đạt được bằng cách chọn các vật phẩm cho bài toán knapsack bằng phương pháp tìm kiếm brute force.
    """
    num_items = len(values)
    max_value = 0
    max_subset = None

    # Tạo tất cả các tập con có thể của các vật phẩm
    for i in range(2**num_items):
        subset = []
        for j in range(num_items):
            if i & (1 << j):
                subset.append(j)

        # Kiểm tra xem tập con có ít nhất 1 món hàng từ mỗi class chưa
        # Tạo một dict để đếm số lượng món hàng từ mỗi class trong tập con
        # class_counts = {class_label: 0 for class_label in set(class_labels)}
        # for index in subset:
        #     if class_labels[index] <= m:
        #         class_counts[class_labels[index]] += 1
        # if any(count == 0 for class_label, count in class_counts.items() if class_label <= m):
        #     continue
        total_value = 0
        total_weight = 0
        class_items = {i: False for i in range(1, m + 1)}
        for index in subset:
            class_items[class_labels[index]] = True
        if total_weight > capacity or False in class_items.values():
            continue


        # Tính tổng giá trị và trọng lượng của tập con
        
        for index in subset:
            total_value += values[index]
            total_weight += weights[index]

        # Kiểm tra xem tập con có thể chứa trong knapsack và có giá trị lớn hơn không
        if total_weight <= capacity and total_value > max_value and len(subset):
            max_value = total_value
            max_subset = subset
    return max_value, max_subset



def read_input_file(filename):
    with open(filename, 'r') as f:
        # Read the Knapsack's storage capacity (W)
        capacity = float(f.readline().strip())

        # Read the number of classes (m)
        num_classes = int(f.readline().strip())

        # Read the weights of n items in floating point numbers (w)
        weights = list(map(float, f.readline().strip().split(',')))

        # Read the values of n items in integers (v)
        values = list(map(int, f.readline().strip().split(',')))

        # Read the class label of each item in the order (c_i)
        class_labels = list(map(int, f.readline().strip().split(',')))

    return capacity, num_classes, weights, values, class_labels

def write_output_file(filename, max_value, max_subset, num_items):
    with open(filename, 'w') as f:
        # Write a sequence of 0s and 1s representing which items in n items
        # are placed in the Knapsack
        if max_subset is None:
            f.write("No valid subset found")
        else:
            # Write the highest total value of the filled Knapsack
            f.write(str(max_value) + "\n")
            subset_str = [str(int(i in max_subset)) for i in range(num_items)]
            f.write(", ".join(subset_str) + "\n")

def main(input_file, output_file):
    # Read input file
    capacity, num_classes, weights, values, class_labels = read_input_file(input_file)

    # Solve knapsack problem
    max_value, max_subset = knapsack_brute_force_searching(capacity, num_classes, weights, values, class_labels)

    # Write output file
    write_output_file(output_file, max_value, max_subset, len(values))


if __name__ == '__main__':
    main('INPUT_2.txt', 'OUTPUT_2.txt')

