import math


def num_pies(arr: list, n: int) -> int:
    total_pieces = 0
    for i in arr:
        total_pieces += i['num']
    return math.ceil(total_pieces/n)


print(num_pies(
    [{"name": "Joe", "num": 9},
     {"name": "Cami", "num": 3},
     {"name": "Cassidy", "num": 4}],
    8))
