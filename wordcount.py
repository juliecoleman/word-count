def count_words_in_file(filename):

    lines = open(filename)

    word_counts = {}


    for line in lines:

        words = line.split(" ")

        print(words)

        for word in words:

            word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

print(count_words_in_file("test.txt"))
print(count_words_in_file("twain.txt"))
