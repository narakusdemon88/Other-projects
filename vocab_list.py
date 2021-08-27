import random

k = 20
filename = 'jlpt_list_script.txt'
with open(filename, encoding='utf8') as file:
    lines = file.read().splitlines()

if len(lines) > k:
    random_lines = random.sample(lines, k)
    print("\n".join(random_lines)) # print random lines
