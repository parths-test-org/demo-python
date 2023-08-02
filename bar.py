import os

breakpoint()


def foo(a=None):
    print("abc")
    breakpoint()


def bar(z=[]):
    print("useless")
    assert z
