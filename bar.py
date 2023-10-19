import os


def foo(a=None):
    breakpoint()
    print("abc")


def bar(z=None):
    print("useless")
    assert z
