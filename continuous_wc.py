#!/usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        print(line, flush=True, end='')

if __name__=='__main__':
    main()