import os

breakpoint()


def foo(a=None):
    breakpoint()
    print("abc")


def bar(z=[]):
    breakpoint()
    print("useless")
    assert z


def baz(x=[]):
    breakpoint()
    print("abc")
