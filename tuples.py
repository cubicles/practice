# Tuples are lists cousins
my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3

try:
    my_tuple[1] = 3
except TypeError:
    print('cant modify the tuple :(')

# Can be used for returning multiples values
# En el BBVA use notebooks y sin saber usaba tuplas sin '('


def sum_and_product(x, y):
    return (x + y), (x * y)

sp = sum_and_product(2, 3)      # sp = (5, 6) (tuple)
s, p = sum_and_product(5, 10)   # s = 15, p = 50

