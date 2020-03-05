#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2020-02-05
Purpose: My Favorite Things
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='My Favorite Things',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('things', metavar='str', nargs='+', help='Some things')

    parser.add_argument('-s',
                        '--sep',
                        help='A separator',
                        metavar='str',
                        type=str,
                        default=', ')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    print(args.sep.join(args.things))

    if len(args.things) == 1:
        print('This is one of my favorite things.')
    else:
        print('These are a few of my favorite things.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
