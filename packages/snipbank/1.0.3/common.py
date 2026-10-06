import os
import yaml

def getDefaultData():
    '''
    Return YAML data for an empty match file.
    '''
    return {"matches": []}

def getSnipBankRoot():
    '''
    Return the default root directory, creating it if it does not already exist.
    '''
    root = os.path.join(os.path.dirname(__file__), '..', 'snipbank_generated')
    if not os.path.isdir(root):
        os.mkdir(root)
    return root

def getSnipBankRootFile():
    '''
    Return the default generated file, creating it if it does not already exist.
    '''
    rootFile = os.path.join(getSnipBankRoot(), 'generated.yml')
    if not os.path.isfile(rootFile):
        with open(rootFile, 'w') as rootFh:
            yaml.dump(getDefaultData(), rootFh)
    return rootFile
