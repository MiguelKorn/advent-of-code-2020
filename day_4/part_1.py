input = open('input.txt', 'r')
input_list = input.read().split('\n\n')
print(input_list)

valid = 0
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for p in input_list:
    d = dict(map(lambda x: x.split(':'), p.split()))
    if all(f in d for f in fields):
        valid += 1
print(valid)