#!/usr/bin/env python3
"""Count UTF-8 prompt body from file or stdin; fail if over limit."""
import argparse
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', nargs='?', help='UTF-8 prompt body; omit for stdin')
    parser.add_argument('--limit', type=int, default=1024)
    args = parser.parse_args()
    if args.limit < 1:
        parser.error('--limit must be positive')
    text = Path(args.path).read_text(encoding='utf-8') if args.path else sys.stdin.read()
    count = len(text)
    utf16 = len(text.encode('utf-16-le')) // 2
    passed = max(count, utf16) <= args.limit
    print(f'characters={count}, utf16_units={utf16}, limit={args.limit}, ' + ('PASS' if passed else 'FAIL'))
    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(main())
