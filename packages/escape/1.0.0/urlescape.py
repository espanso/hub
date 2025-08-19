import sys
from urllib.parse import quote_plus as escape

if __name__ == '__main__':
    print(escape(sys.argv[1]), end='')
