from functools import reduce

# lamda arguments: expression
# sort: It modifies the list
# sorted: It return a new list
points2D = [(1, 2), (15, 1), (5, -1)]
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)] => sort by age


# map(fun, iter)
numbers = (1, 2, 3, 4)
result1 = map(lambda num: num + num, numbers)
result2 = [x*2 for x in numbers]  # list comprehension
print(list(result1))
print(result2)

# filter(fun, iter)
result3 = filter(lambda num: num % 2 == 0, numbers)
result4 = [x for x in numbers if x % 2 == 0]  # list comprehension
print(list(result3))
print(list(result4))

# reduce(fun, iter)
result5 = reduce(lambda x, y: x*y, numbers)
print(result5)
