input = open('input.txt', 'r')
input_list = input.read().split('\n')

counts = []
for step_x, step_y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    x = 0
    y = 0
    maxLen = len(input_list[0])
    c = 0

    while y < len(input_list) - 1:
        x = (x + step_x) % maxLen
        y += step_y
        if input_list[y][x] == '#':
            c += 1
    counts.append(c)
print(counts)

x = 1
for y in counts:
    x *= y
print(x)
