import sys, json

def fillTemplate(template, placeholderFormat, item):
    '''
    Fill the template with the given item list, and return the result.
    '''
    result = template
    for i in range(len(item)):
        result = result.replace(placeholderFormat.replace('N', str(i)), item[i])
    return result

if __name__ == '__main__':
    # Syntax: foreach_ext.py <template> <placeholderformat> <rowseparator> <columnseparator> <items> <itemseparator>
    template = sys.argv[1]
    placeholderFormat = sys.argv[2]
    rowSeparator = json.loads('"%s"' % (sys.argv[3]))
    columnSeparator = json.loads('"%s"' % (sys.argv[4]))
    items = [rowString.split(columnSeparator) for rowString in sys.argv[5].split(rowSeparator)]
    itemSeparator = json.loads('"%s"' % (sys.argv[6]))
    print(itemSeparator.join([fillTemplate(template, placeholderFormat, item) for item in items]), end='')
