import re
import sys
import yaml
from common import *

formPrefix = 'f'

def getEspansoFormVar(formText, name=formPrefix):
    '''
    Return the Espanso form variable specification of the given form text.
    [[field=default]]: Regular text field
    [![field=default]!]: Text area
    [^[field=default:opt0|opt1|opt2|...]^]: Dropdown
    [>[field=default:opt0|opt1|opt2|...]<]: Multi-select
    '''
    fields = {}
    layout = formText
    textFieldRegex = re.compile(r'\[\[([\w_]+)(=?[^\]]*)\]\]')
    textAreaRegex = re.compile(r'\[\!\[([\w_]+)(=?[^\]]*)\]\!\]')
    dropdownRegex = re.compile(r'\[\^\[([\w_]+)(=?[^:]*):([^\]]*)\]\^\]')
    listSelectRegex = re.compile(r'\[\>\[([\w_]+)(=?[^:]*):([^\]]*)\]\<\]')
    
    # Populate fields
    for match in textFieldRegex.finditer(formText):
        fieldName = match[1]
        fieldDefault = match[2][1:]
        if fieldDefault:
            fields[fieldName] = {
                "default": fieldDefault
            }
    for match in textAreaRegex.finditer(formText):
        fieldName = match[1]
        fieldDefault = match[2][1:]
        fields[fieldName] = {
            "multiline": True,
            "default": fieldDefault
        }
    for match in dropdownRegex.finditer(formText):
        fieldName = match[1]
        fieldDefault = match[2][1:]
        fieldChoices = match[3].split('|')
        fields[fieldName] = {
            "type": "choice",
            "default": fieldDefault,
            "values": fieldChoices
        }
    for match in listSelectRegex.finditer(formText):
        fieldName = match[1]
        fieldDefault = match[2][1:]
        fieldChoices = match[3].split('|')
        fields[fieldName] = {
            "type": "list",
            "default": fieldDefault,
            "values": fieldChoices
        }
    
    # Replace layout elements
    for regex in (textFieldRegex, textAreaRegex, dropdownRegex, listSelectRegex):
        layout = regex.sub('[[\\1]]', layout)

    # Form body
    body = {
        "name": name,
        "type": "form",
        "params": {
            "layout": layout,
            "fields": fields
        }
    }
    return body

def addTrigger(rootFile, trigger, snippet, form, replaceType, reprint=False):
    '''
    Add a regular trigger to a match YAML file.
    '''
    data = getDefaultData()
    rectifiedSnippet = re.sub(r'\{\{([\w_]+)\}\}', '{{' + formPrefix + '.\\1}}', snippet.replace('^TAB^', "\t").replace('^ENTER^', "\n"))
    with open(rootFile, 'r') as rootFh:
        data = yaml.load(rootFh, Loader=yaml.BaseLoader)
    replacement = {
        "trigger": trigger,
        replaceType: rectifiedSnippet,
    }
    if form:
        replacement['vars'] = [getEspansoFormVar(form)]
    data['matches'].append(replacement)
    data['matches'].sort(key=lambda m : m['trigger'].upper())
    with open(rootFile, 'w') as rootFh:
        yaml.dump(data, rootFh)
    if reprint:
        print(rectifiedSnippet, end='')

if __name__ == '__main__':
    # Syntax: python3 addtrigger.py <trigger> <snippet> <form> <replacetype> <paste|silent>
    if not sys.argv[1]:
        exit(0)
    addTrigger(getSnipBankRootFile(), sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], reprint=sys.argv[5] == 'paste' and not sys.argv[3])
