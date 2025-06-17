import random
import datetime
import os
import subprocess
import json

# region Dependency Definitions
class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data

class LinkedList:
    head: Node = None
    tail: Node = None

    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def __iter__(self):
        return LinkedListIterator(self)
    
    def __add__(self, other):
        result: LinkedList = LinkedList()
        result.appendNode(self.head)
        result.appendNode(other.head)
        
        return result

    def prepend(self, value):
        self.prependNode(Node(value))

        return

    def prependNode(self, node: Node):
        temp: Node = self.head
        self.head = node
        self.head.next = temp

        if (self.tail is None):        
            self.tail = self.head

        while (self.tail.next is not None):
            self.tail = self.tail.next

        return

    def append(self, value):
        self.appendNode(Node(value))

        return

    def appendNode(self, node: Node):
        if (self.head is None):
            self.head = node
            self.tail = self.head

            while (self.tail.next is not None):
                self.tail = self.tail.next
  
            return
        
        if (self.tail is None):
            self.tail = self.head

        while (self.tail.next is not None):
            self.tail = self.tail.next

        self.tail.next = node
        self.tail = self.tail.next

        return

class LinkedListIterator:
    iterator: Node = None

    def __init__(self, list: LinkedList):
        self.iterator = list.head

    def __next__(self):
        if (self.iterator is None):
            raise StopIteration

        item = self.iterator.data
        
        self.iterator = self.iterator.next

        return item
    
# endregion

# region Main Program
tagChar: str = ':'

tagged: LinkedList = LinkedList()
shuffle: LinkedList = LinkedList()

personalGreetings = list()
generalGreetings = list()
mondayGreetings = list()
fridayGreetings = list()

config = json.loads(open(file=os.path.join(os.path.dirname(__file__), "config.json"), encoding="utf-8-sig").read())

# For each name in the names file, check to see if the name includes tagChr. If the name is tagged, add it to the tagged list in the 
# order it appears in the original file. Otherwise, either append or prepend the name to the shuffle list depending on whether a 
# random value between 0 and 99 is even or odd. This builds the list in a semi-random order and prevents the need to shuffle the 
# values later on:
for name in open(file=os.path.join(os.path.dirname(__file__), "names.txt"), encoding="utf-8-sig"):
    if (name.__contains__(tagChar)):
        tagged.append(name[name.index(tagChar)+ 1:].rstrip())
    elif (random.randint(0, 99) % 2 == 0):
        shuffle.append(name.rstrip())
    else:
        shuffle.prepend(name.rstrip())

for greeting in config["personalGreetings"]:
    personalGreetings.append(greeting.rstrip())

for greeting in config["weekdayGreetings"]:
    generalGreetings.append(greeting.rstrip())

for greeting in config["mondayGreetings"]:
    mondayGreetings.append(greeting.rstrip())

for greeting in config["fridayGreetings"]:
    fridayGreetings.append(greeting.rstrip())

for name in (tagged + shuffle):
    print(f"{personalGreetings[random.randint(0, personalGreetings.__len__() - 1)]} {name}!")

if (datetime.date.today().weekday() == 0):
    print(f"\n{mondayGreetings[random.randint(0, mondayGreetings.__len__() - 1)]}")
elif (datetime.date.today().weekday() == 4):
    print(f"\n{fridayGreetings[random.randint(0, fridayGreetings.__len__() - 1)]}")    
else:
    print(f"\n{generalGreetings[0]}")

if (config["downloadImage"]):
    # Uses GitHub API to pull list of images in gif directory of repository. This can be used to dynamically obtain the total number of 
    # images in the directory later:

    try:
        listURL =  "https://api.github.com/repos/" + config["repo"] + "/contents" + f"/{config["path"]}" if config["path"] != "" else "" + f"?ref={config["branch"]}" if config["branch"] != "" else ""
        gifList = json.loads(subprocess.run(["curl", "-s", listURL, "--ssl-no-revoke", "-H", "Accept: application/json"], capture_output=True).stdout.decode())
    
    except Exception as ex:
        print(f"Failed to download list of repository content. Check \"repo\" and \"path\" values in config.json:\n{ex}")

    # Attempt to curl a random gif from the gif directory
    try:
        downloadURL = gifList[random.randint(1, gifList.__len__() - 1)]["download_url"] 
        subprocess.run(["curl", "-s", downloadURL, "--ssl-no-revoke", "-H", "Accept: image/*","-o", os.path.join(os.path.dirname(__file__), "tmp.gif")])

    except Exception as ex:
        print(f"Failed to download GIF image:\n{ex}")

# endregion