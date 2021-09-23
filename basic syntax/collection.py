from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Conter
a = 'aaaabbc'
counter = Counter(a)
print(counter)  # Counter({'a': 4, 'b': 2, 'c': 1})
print(counter.items())  # dict_items([('a', 4), ('b', 2), ('c', 1)])
print(counter.keys())  # dict_keys(['a', 'b', 'c'])
print(counter.values())  # dict_values([4, 2, 1])
print(counter.most_common(1)[0][0])  # 'a'
print(list(counter.elements()))  # ['a', 'a', 'a', 'a', 'b', 'b', 'c']

# OrderedDict
d = OrderedDict([('a', 1), ('b', 2)])
d.update({'c': 3})
print(d.popitem(last=True))  # pop last item
print(d.popitem(last=False))  # pop first item
d.move_to_end('b', last=True)  # move to last
d.move_to_end('b', last=False)  # move to first

# DefaultDict


def letterCounter(word):
    counter = defaultdict(int)
    for letter in word:
        counter[letter] += 1
    return counter


# namedtuple
normal_tuple = ('Suyeon', '23', '2541997')
Student = namedtuple('Student', ['name', 'age', 'DOB'])
s = Student('Suyeon', '23', '2541997')

print(normal_tuple)
print(s)
print(s[1])
print(s.name)

# Deque
queue = deque([1, 2, 3])
queue.append(4)  # insert to right
queue.appendleft(0)  # insert to left
queue.pop()  # delete from right
queue.popleft()  # delete from left
print(queue)
