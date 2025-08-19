import sys
from urllib.parse import unquote_plus as unescape

if __name__ == '__main__':
    print(unescape(sys.argv[1]), end='')
