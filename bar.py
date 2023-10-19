import os


def foo(a=None):
    breakpoint()
    print("abc")


def bar(z=[]):
    print("useless")
    assert z
