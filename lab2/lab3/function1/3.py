def solve(numheads, numlegs):
    for numrabbits in range(numheads + 1):
        numchickens = numheads - numrabbits
        if (4 * numrabbits + 2 * numchickens) == numlegs:
            return numrabbits, numchickens
    return "error"

numheads = 35
numlegs = 94

result = solve(numheads, numlegs)
print(f"Количество кроликов: {result[0]}")
print(f"Количество цыплят: {result[1]}")
