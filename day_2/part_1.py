input = open('input.txt', 'r')
input_list = input.read().split('\n')

correct = 0
for p in input_list:
    p = p.split()
    min, max = p[0].split('-')
    c = p[2].count(p[1][0])
    if int(min) <= c <= int(max):
        correct += 1
print(correct)