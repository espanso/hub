import sys
import yaml
from common import *

def listTriggers(rootFile):
    '''
    Print all triggers line-by-line.
    '''
    data = getDefaultData()
    with open(rootFile, 'r') as rootFh:
        data = yaml.load(rootFh, Loader=yaml.BaseLoader)
    for match in data['matches']:
        print(match['trigger'])

if __name__ == '__main__':
    # Syntax: python3 listtriggers.py
    listTriggers(getSnipBankRootFile())
