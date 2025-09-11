import sys
from json import loads as unescape

if __name__ == '__main__':
    print(unescape('"%s"' % (sys.argv[1])), end='')
