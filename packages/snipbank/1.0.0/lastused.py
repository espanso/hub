import json
import os, sys

def getDefaultData():
    '''
    Return JSON data for an empty last-used file.
    '''
    return {}

def getLastUsedDirectory():
    '''
    Return the default last-used directory, creating it if it does not already exist.
    '''
    currentDirectoryName = os.path.dirname(os.path.abspath(__file__))
    lastUsed = os.path.join(currentDirectoryName, '..', os.path.basename(currentDirectoryName) + '_lastused')
    if not os.path.isdir(lastUsed):
        os.mkdir(lastUsed)
    return lastUsed

def getLastUsedRootFile():
    '''
    Return the default last-used file, creating it if it does not already exist.
    '''
    lastUsedFile = os.path.join(getLastUsedDirectory(), 'lastused.json')
    if not os.path.isfile(lastUsedFile):
        with open(lastUsedFile, 'w') as lastUsedFh:
            json.dump(getDefaultData(), lastUsedFh)
    return lastUsedFile

def setProperty(property, value, file=getLastUsedRootFile()):
    '''
    Set the given property value as last-used and save it.
    '''
    data = getDefaultData()
    with open(file, 'r') as f:
        data = json.load(f)
    data[property] = value
    with open(file, 'w') as f:
        json.dump(data, f)

def getProperty(property, defaultValue='', file=getLastUsedRootFile()):
    '''
    Get the given last-used value. If it doesn't exist yet, return the default value.
    '''
    with open(file, 'r') as f:
        data = json.load(f)
    if property in data:
        return data[property]
    return defaultValue


if __name__ == '__main__':
    # Syntax: python3 lastused.py get <name> <defaultvalue>
    if sys.argv[1] == 'get':
        print(getProperty(sys.argv[2], sys.argv[3]), end='')
    # Syntax: python3 lastused.py set <name> <value>
    elif sys.argv[1] == 'set':
        setProperty(sys.argv[2], sys.argv[3])
