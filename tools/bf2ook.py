#!/usr/bin/env python3
"""Transliterate a pure 8-command Brainfuck program into Ook!.

Usage: python3 tools/bf2ook.py json2dir.bf > json2dir.ook

Every Brainfuck command becomes one Ook! word pair; all other characters
(comments) are dropped. Eight pairs per line.
"""
import sys

OOK = {
    '>': 'Ook. Ook?',
    '<': 'Ook? Ook.',
    '+': 'Ook. Ook.',
    '-': 'Ook! Ook!',
    '.': 'Ook! Ook.',
    ',': 'Ook. Ook!',
    '[': 'Ook! Ook?',
    ']': 'Ook? Ook!',
}


def main(argv):
    if len(argv) != 2:
        sys.stderr.write('usage: bf2ook.py PROGRAM.bf\n')
        return 2
    with open(argv[1], 'rb') as f:
        src = f.read().decode('latin-1')
    pairs = [OOK[c] for c in src if c in OOK]
    out = sys.stdout
    for i in range(0, len(pairs), 8):
        out.write(' '.join(pairs[i:i + 8]) + '\n')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
