#!/usr/bin/env python3
"""tests for hamming.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './hamming.py'


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
def test_bad_file():
    """Bad file"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def run(input_file, expected, min_val):
    """run on input"""

    min_flag = '-m' if random.choice([0, 1]) else '--min'
    min_arg = f'{min_flag} {min_val}' if min_val else ''
    rv, out = getstatusoutput(f'{prg} {min_arg} {input_file}')
    assert rv == 0
    assert out.rstrip() == expected.rstrip()


# --------------------------------------------------
def test_input1():
    """input1"""

    run('input1.txt', '       1:foo                 boo', 0)


# --------------------------------------------------
def test_input2():
    """input2"""

    expected = '\n'.join([
        '       1:foo                 boo                 ',
        '       2:foo                 faa                 ',
        '       3:foo                 foobar              ',
    ])

    run('input2.txt', expected, 0)


# --------------------------------------------------
def test_input3():
    """input3"""

    expected = '\n'.join([
        '       9:TAGGGCAATCATCCGAG   ACCGTCAGTAATGCTAC   ',
        '      10:TAGGGCAATCATCCGG    ACCGTCAGTAATGCTAC   ',
    ])

    run('input3.txt', expected, 0)


# --------------------------------------------------
def test_input2_min2():
    """input2 min 2"""

    expected = '\n'.join([
        '       2:foo                 faa                 ',
        '       3:foo                 foobar              ',
    ])

    run('input2.txt', expected, 2)


# --------------------------------------------------
def test_input3_min10():
    """input3"""

    run('input3.txt', '      10:TAGGGCAATCATCCGG    ACCGTCAGTAATGCTAC   ', 10)


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
