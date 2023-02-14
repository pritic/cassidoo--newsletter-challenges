# Spreadsheet programs often use the A1 Reference Style to refer to columns. Given a column name in this style, return its column number. 

# Examples of column names to their numbers: 

# A -> 1
# B -> 2
# C -> 3
# // etc
# Z -> 26
# AA -> 27
# AB -> 28
# ...
# AZ ->
# BA -> BZ ... ZZ ... AAA
# // etc
# AAA -> 703
# AAAA

# https://github.com/szkjn/algorithmic-exercises/blob/main/get_a1_ref_num.py

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_column_number(name: str) -> int:
    col_num = 0
    for c in name:
        col_num = col_num * len(alphabet) + alphabet.index(c) + 1
    return col_num

print(get_column_number("A"))
print(get_column_number("BA"))
print(get_column_number("BZ"))
print(get_column_number("ZZ"))
print(get_column_number("ICD"))
print(get_column_number("AAAB"))
