#!/usr/bin/env python3
""" Hamming distance """

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='File inputs')

    parser.add_argument('-m',
                        '--min',
                        metavar='int',
                        type=int,
                        default=0,
                        help='Minimum distance to show')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in args.file:
        word1, word2 = line.rstrip().split()
        distance = dist(word1, word2)
        if distance >= args.min:
            print(f'{distance:8}:{word1:20}{word2:20}')


# --------------------------------------------------
def dist(s1, s2):
    """ Find hamming distance b/w two strings """

    # The base distance is the difference in their lengths
    l1, l2 = len(s1), len(s2)
    distance = abs(l1 - l2)

    # Use zip to pair up the letters
    for char1, char2 in zip(s1, s2):
        print(char1, char2)
        if char1 != char2:
            distance += 1

    return distance


# --------------------------------------------------
def test_dist():
    """dist ok"""

    assert dist('foo', 'boo') == 1
    assert dist('foo', 'faa') == 2
    assert dist('foo', 'foobar') == 3
    assert dist('TAGGGCAATCATCCGAG', 'ACCGTCAGTAATGCTAC') == 9
    assert dist('TAGGGCAATCATCCGG', 'ACCGTCAGTAATGCTAC') == 10


# --------------------------------------------------
if __name__ == '__main__':
    main()
