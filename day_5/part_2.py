input = open('input.txt', 'r')
input_list = input.read().split('\n')
print(input_list)

highest = 0
seats = []
for p in input_list:
    p = p.replace('B', '1')
    p = p.replace('R', '1')
    p = p.replace('F', '0')
    p = p.replace('L', '0')
    total = int(p[:-3], 2) * 8 + int(p[-3:], 2)
    print(int(p[:-3], 2), int(p[-3:], 2), total)
    seats.append(total)
    if total > highest:
        highest = total
print(highest)
seats.sort()


for x in range(seats[0], seats[-1]):
    if x not in seats and x+1 in seats and x-1 in seats:
        print(x)