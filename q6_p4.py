def count_pattern_helper(ord_str):
    ord_list = []
    for i in range(0, len(ord_str) - 1):
        ord_list.append(ord(ord_str[i]) - ord(ord_str[i + 1]))
    return ord_list


def count_pattern(str, pattern, replace_str):

    assert len(str) >= len(pattern)
    replaced_str = str[:]
    location_of_pattern = []
    str_list = list(replaced_str)

    # Find the ordinance of the pattern to check against str
    ordinance_list = count_pattern_helper(pattern)
    # print(ordinance_list)

    j = 0
    for i in range(0, len(str_list) - 1):
        if ord(str_list[i]) - ord(str_list[i + 1]) == ordinance_list[j]:
            # Need to have a check
            if count_pattern_helper(str_list[i:i + len(pattern)]) == ordinance_list:
                location_of_pattern.append(str_list[i:i + len(pattern)])
            else:
                continue

    # print(location_of_pattern)

    for k in range(0, len(location_of_pattern)):
        replaced_str = replaced_str.replace("".join(location_of_pattern[k]), replace_str)
    return replaced_str


print(count_pattern("shihfdddedaaba", "xyx", "123"))
