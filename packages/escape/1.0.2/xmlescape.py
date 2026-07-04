import sys
from xml.sax.saxutils import escape

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print(escape(sys.argv[1]), end='')
