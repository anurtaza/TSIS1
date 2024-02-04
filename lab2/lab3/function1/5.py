def generate_permutations(string):
    if len(string) == 0:
        return []
    elif len(string) == 1:
        return [string]
    else:
        permutations = []
        for i in range(len(string)):
            char = string[i]
            remaining_chars = string[:i] + string[i+1:]
            for permutation in generate_permutations(remaining_chars):
                permutations.append(char + permutation)
        return permutations

# Example usage
user_input = input()
permutations = generate_permutations(user_input)
print(permutations)
