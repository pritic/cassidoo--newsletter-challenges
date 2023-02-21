# Given a string of parenthesis, return the number of parenthesis
# you need to add to the string in order for it to be balanced.

# Examples:

# > numBalanced(`()`)
# > 0

# > numBalanced(`(()`)
# > 1

# > numBalanced(`))()))))()`)
# > 6

# > numBalanced(`)))))`)
# > 5


def num_balanced(s: str) -> int:
    result = 0

    for i in s:
        if i == '(':
            result += 1
        if i == ')':
            result -= 1

    return abs(result)

print(num_balanced('()'))
print(num_balanced('(()'))
print(num_balanced('))()))))()'))
print(num_balanced(')))))'))

print(num_balanced(''))
print(num_balanced('(((())))'))
print(num_balanced('(((('))
