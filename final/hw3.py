def permutations(arr):
    result = []

    def generate_permutations(current_permutation, remaining_elements):
        if not remaining_elements:
            result.append(current_permutation[:])
            return

        for i in range(len(remaining_elements)):
            current_permutation.append(remaining_elements[i])
            next_elements = remaining_elements[:i] + remaining_elements[i + 1:]
            generate_permutations(current_permutation, next_elements)
            current_permutation.pop()

    generate_permutations([], arr)
    return result

input_list = [1, 2, 3]
all_permutations = permutations(input_list)

for perm in all_permutations:
    print(perm)

#This program defines a permutations function that uses recursion to generate all possible permutations. You can replace input_list with the list of permutations you want to generate.