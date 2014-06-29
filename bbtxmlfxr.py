#!/usr/bin/env python3

import sys

# sorry, I'm too lazy to write more graceful
# error handling right now
if 2 != len(sys.argv):
    print("you did something wrong")
    sys.exit(1)

