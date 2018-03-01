def count_pattern(str, pattern, replace_str):
    assert len(str) >= len(pattern)

    str_list = list(str)
    pattern_list = list(pattern)
    replace_str_list = list(replace_str)
    indexes = []

    # Locate where the pattern is in the original string
    for i in range(0, len(str_list)):
        for j in range(0, len(pattern_list)):
            if str_list[i] == pattern_list[j]:
                indexes.append(i)




print(count_pattern("hello", "yo", "this"))
