def check_007(lst):
    for i in range(len(lst) - 2):
        if lst[i] == 0 and lst[i+1] == 0 and lst[i+2] == 7:
            return True
    return False

numbers = [1, 2, 0, 0, 7, 8, 9]
result = check_007(numbers)
print(result)  # True