def count_pattern_helper(ord_str):
    ord_list = []
    for i in range(0, len(ord_str) - 1):
        ord_list.append(ord(ord_str[i]) - ord(ord_str[i+1]))
    return ord_list

def count_pattern(str, pattern, replace_str):
    assert len(str) >= len(pattern)
    ordinance_list = []
    location_of_pattern = []
    str_list = list(str)
    pattern_list = list(pattern)
    replace_str_list = list(replace_str)

    # Find the ordinance of the pattern to check against str
    ordinance_list = count_pattern_helper(pattern)
    print(ordinance_list)

    j = 0
    for i in range(0, len(str_list) - 1):
        if ord(str_list[i]) - ord(str_list[i+1]) == ordinance_list[j]:
            # Need to have a check
            if count_pattern_helper(str_list[i:i + len(pattern)]) == ordinance_list:
                location_of_pattern.append(str_list[i:i + len(pattern)])

    print(location_of_pattern)






count_pattern("ahihfdddedaaba", "xyx", "123")