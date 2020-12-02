input = open('input.txt', 'r')
input_list = input.read().split('\n')

correct = 0
for p in input_list:
    p = p.split()
    min, max = p[0].split('-')
    l = p[1][0]
    s = p[2]
    if (s[int(min) - 1] == l) != (s[int(max) - 1] == l):
        correct += 1
print(correct)