from q4_p1 import word_count

top_10_words = open("top10words.txt", "w")
word_dict = word_count()
top_word_list = []
index = 1

if len(word_dict) <= 10:
    for word, occurrence in sorted(word_dict.items(), key=lambda x: x[1], reverse=True):
        top_10_words.write(word + ", " + str(occurrence) + "\n")
else:
    for word, occurrence in sorted(word_dict.items(), key=lambda x: x[1], reverse=True):
        if index <= 10:
            top_10_words.write(word + ", " + str(occurrence) + "\n")
            index += 1
        else:
            break
