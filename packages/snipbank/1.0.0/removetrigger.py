import sys
import yaml
from common import *

def removeTrigger(rootFile, trigger):
    '''
    Remove the given trigger from the match YAML file.
    '''
    data = getDefaultData()
    with open(rootFile, 'r') as rootFh:
        data = yaml.load(rootFh, Loader=yaml.BaseLoader)
    data['matches'] = [match for match in data['matches'] if match['trigger'] != trigger]
    with open(rootFile, 'w') as rootFh:
        yaml.dump(data, rootFh)

def getTriggerReplacement(rootFile, trigger):
    '''
    Return the replacement for the given trigger.
    '''
    with open(rootFile, 'r') as rootFh:
        data = yaml.load(rootFh, Loader=yaml.BaseLoader)
    for match in data['matches']:
        if match['trigger'] == trigger:
            return match['replace'] if 'vars' not in match else ''
    return ''

if __name__ == '__main__':
    # Syntax: python3 removetrigger.py <trigger> <paste|silent>
    if not sys.argv[1].strip():
        exit(0)
    rootFile = getSnipBankRootFile()
    if sys.argv[2] == 'paste':
        print(getTriggerReplacement(rootFile, sys.argv[1]), end='')
    removeTrigger(rootFile, sys.argv[1])
