import sys
import inflect

if len(sys.argv) < 2:
    sys.exit("too few arguments")

for name in sys.argv[1 : +1]:
    print()
