
# Create a function (or write a script in Shell) that takes an integer as an argument
# and returns "Even" for even numbers or "Odd" for odd numbers.

from typing import Iterable


def iterable(func):
    def wrapped(args):
        if isinstance(args, Iterable):
            return [func(a) for a in args]
        else:
            return func(args)
    return wrapped


@iterable
def func(args):
    return 'ODD' if args % 2 else 'EVEN'


print(func(1))
print(func(2))
print(func(range(5)))

