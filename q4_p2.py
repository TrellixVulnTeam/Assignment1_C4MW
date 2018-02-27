from q4_p1 import word_count

articles = open("top10articles.txt", "w")
word_dict = word_count()


for key in word_dict:
    if word_dict[key] > 2:
        print(key)

print(len(word_dict))


