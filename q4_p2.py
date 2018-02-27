from q4_p1 import word_count

top_10_words = open("top10words.txt", "w")
word_dict = word_count()
top_word_list = []
index = 1

if len(word_dict) <= 10:
    for k, v in sorted(word_dict.items(), key=lambda p: p[1], reverse=True):
        top_10_words.write(k + ", " + str(v) + "\n")
else:
    for k, v in sorted(word_dict.items(), key=lambda p: p[1], reverse=True):
        if index <= 10:
            top_10_words.write(k + ", " + str(v) + "\n")
            index += 1
