# Given a positive integer, generate an array in which every
# element is an array that goes from 1 to the index of that array.

# Example:

# > generate_arrays(4)
# > [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4]]

# > generate_arrays(1)
# > [[1]]


def generate_arrays(num: int):
    result = [[1]]
    if num == 1:
        return result

    for i in range(2, num+1):
        new_arr = result[-1].copy()
        new_arr.append(i)
        result.append(new_arr)

    return result


print(generate_arrays(1))
print(generate_arrays(4))
print(generate_arrays(0))
print(generate_arrays(-4))
print(generate_arrays(6))
