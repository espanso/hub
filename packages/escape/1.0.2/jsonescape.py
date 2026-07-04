import sys
from json import dumps as escape

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print(escape(sys.argv[1])[1:-1], end='')
