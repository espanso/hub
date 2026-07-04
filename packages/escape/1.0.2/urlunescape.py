import sys
from urllib.parse import unquote_plus as unescape

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print(unescape(sys.argv[1]), end='')
