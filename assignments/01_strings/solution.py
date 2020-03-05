#!/usr/bin/env python3
"""
Find position of vowel in string
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find position of vowel in string',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('vowel',
                        metavar='vowel',
                        choices='aeiouAEIOU',
                        help='A vowel to look for')

    parser.add_argument('text',
                        metavar='text',
                        help='The text to search')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    vowel = args.vowel
    text = args.text

    if vowel in text:
        print(f'Found "{vowel}" in "{text}" at index {text.index(vowel)}.')
    else:
        print(f'"{vowel}" is not found in "{text}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
