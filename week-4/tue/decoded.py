my_file = open("encoded_zen_lines.txt", "r")
out_file = open("decoded_zen_lines.txt", "w")
lines = my_file.readlines()

for line in lines:
   words = line.split(" ")
   decoded_line = []
   for word in words:
       decoded_word = ""
       for char in word:
           decoded_word += chr(ord(char)-1)
       decoded_line.append(decoded_word)
   print(" ".join(decoded_line))
   out_file.write(" ".join(decoded_line) + "\n")
my_file.close()
out_file.close()
