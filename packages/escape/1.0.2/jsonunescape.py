import sys
from json import loads as unescape

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print(unescape('"%s"' % (sys.argv[1])), end='')
