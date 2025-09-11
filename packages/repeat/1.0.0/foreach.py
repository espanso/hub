import sys, json

if __name__ == '__main__':
    # Syntax: foreach.py <template> <separator> <placeholder> <items>
    template = sys.argv[1]
    separator = json.loads('"%s"' % (sys.argv[2]))
    placeholder = sys.argv[3]
    items = sys.argv[4].split("\n")
    print(separator.join([template.replace(placeholder, item) for item in items]), end='')
