input = open('input.txt', 'r')
input_list = input.read().split('\n')

highest = 0
seats = [int(p.replace('B', '1').replace('R', '1').replace('F', '0').replace('L', '0'), 2) for p in input_list]
seats.sort()
print(seats[-1])

for x in range(seats[0], seats[-1]):
    if x not in seats and x + 1 in seats and x - 1 in seats:
        print(x)