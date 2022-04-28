integer_list = [1, 2, 3]
heterogeneous_list = ['string', 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]

list_lenght = len(integer_list)
list_sum = sum(integer_list)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# For slicing, use i:j, all elements from i(inclusive) to j(non inclusive)

first_three = x[:3]         # Leaving off start, will use from beginning
three_to_end = x[3:]        # Leaving off end, will slice until the end
on_to_four = x[1:5]         # 5 is non inclusive (1, 2, 3, 4)
last_three = x[-3:]         # From -3 to end = (pos-3, pos-2, pos-1)
without_first_and_last = x[1:-1]
copy_of_x = x[:]            # First to last

# We can use a third argument called "stride" which can be negative
x[0] = 0
every_third = x[::2]        # Every 2,3, etc according to the stride value
five_to_three = x[5:2:-1]   # -1 stride/step



# Check for list membership (is in)
1 in [1, 2, 3]
0 in [1, 2, 3]

# Add items from another collection
x = [1, 2, 3]
x.extend([4, 5, 6]) # Inplace

# Without modifying x
x = [1, 2, 3]
y = x + [4, 5, 6]
print(y)

# Append (common)
x = [1, 2, 3]
x.append(0)
y = x[-1]
z = len(x)

# Unpacking
x, y = [1, 2]
_, y = [3, 4]

