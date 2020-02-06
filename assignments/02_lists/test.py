#!/usr/bin/env python3
"""tests for listy.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './favorite.py'
things = [
    'cake', 'cookies', 'tart', 'pie', 'fudge', 'popsicle', 'brownies',
    'ice cream', 'popover', 'scone'
]
coda_one = '\nThis is one of my favorite things.'
coda = '\nThese are a few of my favorite things.'
seps = ':$#@!'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_one():
    """one thing"""

    arg = random.choice(things)
    rv, out = getstatusoutput(f'{prg} {quote(arg)}')
    assert rv == 0
    assert out == f'{arg}{coda_one}'


# --------------------------------------------------
def test_two():
    """two things"""

    args = random.sample(things, k=2)
    rv, out = getstatusoutput(f'{prg} {" ".join(map(quote, args))}')
    assert rv == 0
    assert out == f'{", ".join(args)}{coda}'


# --------------------------------------------------
def test_two_sep():
    """two things, separator"""

    args = random.sample(things, k=2)
    sep = random.choice(seps)
    rv, out = getstatusoutput(f'{prg} {" ".join(map(quote, args))} -s "{sep}"')
    assert rv == 0
    assert out == f'{sep.join(args)}{coda}'


# --------------------------------------------------
def test_more_than_two_default_sep():
    """more than two things"""

    args = random.sample(things, k=random.randint(3, 7))
    rv, out = getstatusoutput(f'{prg} {" ".join(map(quote, args))}')
    assert rv == 0
    assert out == f'{", ".join(args)}{coda}'


# --------------------------------------------------
def test_more_than_two_sep():
    """more than two things"""

    args = random.sample(things, k=random.randint(3, 7))
    sep = random.choice(seps)
    rv, out = getstatusoutput(
        f'{prg} {" ".join(map(quote, args))} --sep "{sep}"')
    assert rv == 0
    assert out == f'{sep.join(args)}{coda}'


# --------------------------------------------------
def quote(s):
    """quote something"""

    return f'"{s}"'
