#!/usr/bin/env python3
"""tests for vpos.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './vpos.py'


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
def test_bad_vowel():
    """bad vowel"""

    consonants = [c for c in string.ascii_lowercase if c not in 'aeiou']
    bad = random.choice(consonants)
    rv, out = getstatusoutput(f'{prg} {bad} apple')
    assert rv != 0
    assert re.search(f"invalid choice: '{bad}'", out)


# --------------------------------------------------
def test_found_a():
    """lowercase, beginning"""

    rv, out = getstatusoutput(f'{prg} a apple')
    assert rv == 0
    assert out == 'Found "a" in "apple" at index 0.'


# --------------------------------------------------
def test_found_e():
    """lowercase, end"""

    rv, out = getstatusoutput(f'{prg} e apple')
    assert rv == 0
    assert out == 'Found "e" in "apple" at index 4.'


# --------------------------------------------------
def test_found_O():
    """uppercase, middle"""

    rv, out = getstatusoutput(f'{prg} O YELLOW')
    assert rv == 0
    assert out == 'Found "O" in "YELLOW" at index 4.'


# --------------------------------------------------
def test_not_found_lower():
    """not found"""

    rv, out = getstatusoutput(f'{prg} o apple')
    assert rv == 0
    assert out == '"o" is not found in "apple".'


# --------------------------------------------------
def test_not_found_upper():
    """not found"""

    rv, out = getstatusoutput(f'{prg} O BANANA')
    assert rv == 0
    assert out == '"O" is not found in "BANANA".'
