import sys
from xml.sax.saxutils import unescape

if __name__ == '__main__':
    print(unescape(sys.argv[1]), end='')
