
my_file = open("reversed_zen_order.txt", "r")

lines = my_file.readlines()
print(lines)
my_file.close()

reversed_lines = lines[::-1]
# print(lines)

for line in reversed_lines:
    print(line.rstrip())
