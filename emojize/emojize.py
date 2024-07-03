import cowsay
import sys

try:
    if len(sys.argv) < 2:
        print('too few arguments')
    elif len(sys.argv) > 2:
        print('too many arguments')
    else:
        cowsay.trex('hello my name is', sys.argv[1])

except:
    cowsay.cow('Contact customer service')
