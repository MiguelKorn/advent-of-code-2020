input = open('input.txt', 'r')
input_list = input.read().split('\n')

for str_x in input_list:
    x = int(str_x)
    for str_y in input_list:
        y = int(str_y)
        if x != y:
            if x + y == 2020:
                print(x, y)
                print(x * y)