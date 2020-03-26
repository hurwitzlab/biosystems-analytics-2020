#!/usr/bin/env python3
""" Translate DNA/RNA to proteins """

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        type=str,
                        metavar='str',
                        help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seq = args.sequence.upper()

    codon_table = dict()
    for line in args.codons:
        codon, prot = line.upper().rstrip().split()
        codon_table[codon] = prot

    out_fh = args.outfile
    k = 3
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        out_fh.write(codon_table.get(codon, '-'))

    out_fh.write('\n')
    out_fh.close()
    print('Output written to "{}".'.format(args.outfile.name))


# --------------------------------------------------
if __name__ == '__main__':
    main()
