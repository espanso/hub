import sys
from xml.sax.saxutils import unescape

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print(unescape(sys.argv[1]), end='')
