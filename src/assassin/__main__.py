"__main__: generate the list from sys.argv"

import sys

from .assassin import generate

def main(length : int = 3):
    "print a textual representation of a cycle of given length (default 3)"
    for assassin, victime, action in generate(limit=length):
        print(f'{assassin = }')
        print(f'{victime  = }')
        print(f'{action   = }\n')


if len(sys.argv) >= 2:
    main(int(sys.argv[1]))
else:
    main(3)
