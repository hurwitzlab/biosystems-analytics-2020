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

        # The base distance is the difference in their lengths
        l1, l2 = len(word1), len(word2)
        distance = abs(l1 - l2)

        # Use the length of the shortest word
        # Check the letters at each position
        for i in range(min(l1, l2)):
            if word1[i] != word2[i]:
                distance += 1

        # Only print if it's greater or equal to the min
        if distance >= args.min:
            print(f'{distance:8}:{word1:20}{word2:20}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
