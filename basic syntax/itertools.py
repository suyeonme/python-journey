from itertools import product, permutations, combinations, accumulate, groupby, count, cycle, repeat

# (1) product: Cartesian product of input iterables.
a = [1, 2]
b = [3, 4]
prod = product(a, b)
# print(list(prod))  # [(1, 3), (1, 4), (2, 3), (2, 4)]

# (2) permutation: return possible arrangements in a set
c = [6, 1, 2, 3, 4, 5]
perm = permutations(c)
# print(list(perm))
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# (3) combination: Return r length subsequences of elements from the input iterable.
comb = combinations(c, 2)
# print(list(comb))  # [(1, 2), (1, 3), (2, 3)]

# accumulate
acc1 = accumulate(c)
acc2 = accumulate(c, func=max)
# print(list(acc1))  # [1, 3, 6, 10, 15]
# print(list(acc2))  # [6, 1, 2, 3, 4, 5]

# (4) groupby
d = [1, 2, 3, 4, 5]
persons = [{'name': 'Hanna', 'age': 54}, {
    'name': 'Suyeon', 'age': 26}, {'name': 'Sarang', 'age': 20}, {'name': 'Jim', 'age': 20}]

group1 = groupby(d, key=lambda x: x < 3)
group2 = groupby(persons, key=lambda x: x['age'])

for key, value in group1:
    print(key, list(value))

# True [1, 2]
# False [3, 4, 5]

for key, value in group2:
    print(key, list(value))
# 54 [{'name': 'Hanna', 'age': 54}]
# 26 [{'name': 'Suyeon', 'age': 26}]
# 20 [{'name': 'Sarang', 'age': 20}, {'name': 'Jim', 'age': 20}]

# (5) count: infinite loop
for i in count(10):
    print(i)
    if i == 15:
        break
# 10, 11... 15

# (6) cycle: infinite loop
cycle_list = [1, 2, 3]
for i in cycle(cycle_list):
    print(i)
    if i == 3:
        break
# 1,2,3,1,2,3...

# (7) repeat
for i in repeat(1, 4):
    print(i)
# 1,1,1,1
