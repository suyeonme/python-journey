# A decorator is a design pattern that allows a user to add new functionality to an existing object without modifying its structure.
# A decorator takes in a function, adds some functionality and returns it.
# Function is First Class Citizen.

# not using decorator
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")


pretty = make_pretty(ordinary)
pretty()


# using decorator


@make_pretty
def ordinary():
    print("I am ordinary")


ordinary()

# using decorator with parameter


def check_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@check_divide
def divide(a, b):
    print(a/b)

# Chaining decotators


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")
