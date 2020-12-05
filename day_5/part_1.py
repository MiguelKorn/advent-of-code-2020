input = open('input.txt', 'r')
input_list = input.read().split('\n')
print(input_list)

highest = 0
for p in input_list:
    p = p.replace('B', '1')
    p = p.replace('R', '1')
    p = p.replace('F', '0')
    p = p.replace('L', '0')
    total = int(p[:-3], 2) * 8 + int(p[-3:], 2)
    print(int(p[:-3], 2), int(p[-3:], 2), total)
    if total > highest:
        highest = total
print(highest)