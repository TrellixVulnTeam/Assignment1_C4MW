# def count_pattern(str, pattern, replace_str):
#     assert len(str) >= len(pattern)
#     str = str.replace(str, pattern)
#     return str
#
#
# print(count_pattern("hello", "yo", "this"))

def count_pattern(str, pattern, replace_str):
    assert len(str) >= len(pattern)
    str = str.replace(str, pattern)
    return str


print(count_pattern("hello", "yo", "this"))