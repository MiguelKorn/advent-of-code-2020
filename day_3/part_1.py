input = open('input.txt', 'r')
input_list = input.read().split('\n')

x = 0
y = 0
maxLen = len(input_list[0])
c = 0

while y < len(input_list) - 1:
    x = (x + 3) % maxLen
    y += 1
    if input_list[y][x] == '#':
        c += 1
print(c)
