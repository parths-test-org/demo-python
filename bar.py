import os

breakpoint()


def foo(a=None):
    print("abc")


def bar(z=None):
    print("useless")
    assert z


def baz(x=[]):
    breakpoint()
    print("abc")
    return
