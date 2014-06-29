#!/usr/bin/env python3

import sys

# sorry, I'm too lazy to write more graceful
# error handling right now
if 2 != len(sys.argv):
    print("you did something wrong")
    sys.exit(1)

with open(sys.argv[1], 'r') as bibtexfile:
    with open("tmp.bibtex", 'w') as newfile:
        ignore = False
        for line in bibtexfile:
            # ignore abstract and review field
            if 'abstract = {' in line:
                ignore = True
            if 'review = {' in line:
                ignore = True
            if '}' in line:
                ignore = False
            # replacement action
            if not ignore:
                line = line.replace('ä', '{\"a}')
                line = line.replace('ö', '{\"o}')
                line = line.replace('ü', '{\"u}')
                line = line.replace('ß', '{\ss}')
            newfile.write(line)

