input = open('input.txt', 'r')
input_list = input.read().split('\n\n')

print(sum([len(set.intersection(*[set(x) for x in l.split()])) for l in input_list]))