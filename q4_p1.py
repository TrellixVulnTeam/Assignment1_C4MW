def word_count(path):

    try:
        word_count_dict = {}
        # Open the file specified by the user and convert
        f = open(path, "r", encoding="utf8")
        lines = f.readlines()
        for line in lines:
            one_line = line.split(" ")
            for index in range(0, len(one_line)):
                if one_line[index].rstrip() == "":
                    continue
                if one_line[index].rstrip() in word_count_dict:
                    word_count_dict[one_line[index].rstrip()] += 1
                else:
                    word_count_dict[one_line[index].rstrip()] = 1
                index += 1
        print(word_count_dict)
        return word_count_dict
    except IOError as e:
        print("File Not Found")

