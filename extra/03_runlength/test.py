#!/usr/bin/env python3
"""tests for runlength.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './runlength.py'


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
def test_01():
    """test"""

    rv, out = getstatusoutput(f'{prg} A')
    assert rv == 0
    assert out.rstrip() == 'A'

# --------------------------------------------------
def test_02():
    """test"""

    rv, out = getstatusoutput(f'{prg} AA')
    assert rv == 0
    assert out.rstrip() == 'A2'

# --------------------------------------------------
def test_03():
    """test"""

    rv, out = getstatusoutput(f'{prg} AACCC')
    assert rv == 0
    assert out.rstrip() == 'A2C3'

# --------------------------------------------------
def test_04():
    """test"""

    rv, out = getstatusoutput(f'{prg} AACCCGTT')
    assert rv == 0
    assert out.rstrip() == 'A2C3GT2'
