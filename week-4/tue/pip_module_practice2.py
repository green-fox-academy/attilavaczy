encoded_file = open('duplicated_chars.txt', 'r')

# for line in encoded_text:
#     original_line = line.rstrip() #strip?
#     words = original_line_split()
#
#     clean_words = []
#     for word in words:
#         clean_words.append(word[::2])
#
#     print(" ".join(cleaned_words))
#
# encoded_text.close()
#
for line in encoded_file:
    raw_line = line.rstrip()
    cleaned_line = raw_line[::2]
    print(cleaned_line)

encoded_file.close()
