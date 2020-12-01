input = open('input.txt', 'r')
input_list = input.read().split('\n')

for str_x in input_list:
    x = int(str_x)
    for str_y in input_list:
        y = int(str_y)
        for str_z in input_list:
            z = int(str_z)
            if x != y and x != z:
                if x + y + z == 2020:
                    print(x, y, z)
                    print(x * y * z)