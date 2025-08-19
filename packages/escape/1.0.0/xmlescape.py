import sys
from xml.sax.saxutils import escape

if __name__ == '__main__':
    print(escape(sys.argv[1]), end='')
