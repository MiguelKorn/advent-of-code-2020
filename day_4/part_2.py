import re
dir(re)

input = open('input.txt', 'r')
input_list = input.read().split('\n\n')

valid = 0
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for p in input_list:
    d = dict(map(lambda x: x.split(':'), p.split()))
    if all(f in d for f in fields):
        print(d)
        h = d['hgt']
        if 1920 <= int(d['byr']) <= 2002 \
                and 2010 <= int(d['iyr']) <= 2020 \
                and 2020 <= int(d['eyr']) <= 2030 \
                and ((h.endswith("cm") and 150 <= int(h[:-2]) <= 193)
                     or (h.endswith("in") and 59 <= int(h[:-2]) <= 76)) \
                and re.fullmatch(r'#[0-9a-f]{6}', d['hcl']) \
                and d['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] \
                and re.fullmatch(r'[0-9]{9}', d['pid']):
            valid += 1
print(valid)