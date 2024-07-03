import sys
try:
    if sys.argv < 2:
        print('too few arguments')
    elif sys.argv > 2:
        print('too many arguments')
    else:
        print('hello my name is', sys.argv[1])

except:
    print('Contact customer service')
