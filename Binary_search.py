import random

def binary_search(arr, x):
    iterations = 0
    low = 0
    high = len(arr) - 1
    mid = 0
    upper_bound = None

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]
        iterations += 1

        if mid_value < x:
            low = mid + 1
        elif mid_value > x:
            upper_bound = mid_value
            high = mid - 1
        else:
            upper_bound = mid_value
            break

    return iterations, upper_bound

def rand_list():
    new_list = []
    i = 0
    while i < 20:
        fl = round(random.uniform(0, 5), 1)
        new_list.append(fl)
        i += 1
    new_list.sort()
    return new_list

random_list = rand_list()

search_value = round(random.uniform(0, 5), 1)

iterations, upper_bound = binary_search(random_list, search_value)

print(f"list: {random_list}")
if search_value == upper_bound:
    print(f"Element {search_value} found in {iterations} iterations")
else:
    print(f"Element {search_value} not found in list, upper bound in {iterations} iterations: {upper_bound}")


