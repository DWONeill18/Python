# List Comprehension Code Challenge

nums = [4, 8, 15, 16, 23, 42]
double_nums = [2 * i for i in nums]

nums = range(11)
squares = [i**2 for i in nums]

nums = [4, 8, 15, 16, 23, 42]
add_ten = [i + 10 for i in nums]

nums = [4, 8, 15, 16, 23, 42]
divide_by_two = [i / 2 for i in nums]

nums = [4, 8, 15, 16, 23, 42]
parity = [i % 2 for i in nums]

names = ["Elaine", "George", "Jerry", "Cosmo"]
greetings = ["Hello, " + i for i in names]

names = ["Elaine", "George", "Jerry", "Cosmo"]
first_character = [name[0] for name in names]

names = ["Elaine", "George", "Jerry", "Cosmo"]
lengths = [len(name) for name in names]

booleans = [True, False, True]
opposite = [not i for i in booleans]

nums = [5, -10, 40, 20, 0]
greater_than_two = [i > 2 for i in nums]

nested_lists = [[4, 8], [15, 16], [23, 42]]
product = [x * y for (x, y) in nested_lists]

ested_lists = [[4, 8], [16, 15], [23, 42]]
greater_than = [x > y for (x, y) in nested_lists]

nested_lists = [[4, 8], [16, 15], [23, 42]]
first_only = [i[0] for i in nested_lists]

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
sums = [item1 + item2 for (item1, item2) in zip(a, b)]

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
quotients = [item2 / item1 for (item1, item2) in zip(a, b)]

capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]
locations = [capital + ", " + country for (capital, country) in zip(capitals, countries)]

names = ["Shilah", "Arya", "Kele"]
ages = [14, 9, 35]
users = ["Name: " + name + ", Age: " + str(age) for (name, age) in zip(names, ages) ]

a = [30, 42, 10]
b = [15, 16, 17]
greater_than = [item1 > item2 for (item1, item2) in zip(a, b)]



