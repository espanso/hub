import sys, json, itertools

if __name__ == '__main__':
    # Syntax: repeat.py <times> <separator> <texts>
    times = int(sys.argv[1])
    separator = json.loads('"%s"' % (sys.argv[2]))
    text = sys.argv[3]
    print(separator.join(itertools.repeat(text, times)), end='')
