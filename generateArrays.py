# Given a positive integer, generate an array in which every
# element is an array that goes from 1 to the index of that array.

# Example:

# > generateArrays(4)
# > [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4]]

# > generateArrays(1)
# > [[1]]


def generateArrays(num: int):
    result = [[1]]
    if num == 1:
        return result

    for i in range(2, num+1):
        new_arr = result[-1].copy()
        new_arr.append(i)
        result.append(new_arr)

    return result


print(generateArrays(1))
print(generateArrays(4))
