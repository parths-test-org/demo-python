import os

nums = list( range(10))

if a != 1:
    raise   AssertionError
print(b, nums)


def baz(a=None):
    if a is None:
        a = []
    return 0


def aaa(a=None):
    if a is None:
        a = []
    return 1


def foo(b=None):
    if b is None:
        b = []
    return 1


def bar(a):
    return 1


filename = os.tmpnam()
with open(filename, "w") as f:
    pass


def boom(a=None):
    if a is None:
        a = []
    filename = os.tmpnam()
    return filename


s = f"some text that doesn't utilize f string syntax"
