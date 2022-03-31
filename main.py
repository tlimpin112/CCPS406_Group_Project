#from Item import Item, Computer
import Item as I
#import room as R
import player as P
import text as T
import utils
import initialize

rooms = ['Private Workshop']
objects = []
currentroomdict = ['00']

player = P.Player()

def library(string1, string2):
    inputstring = string1+string2
    inputint = int(inputstring)
    
    currentroomdict.append(inputstring)
    #print(inputstring, inputint, initialize.roomdict[inputint][3], rooms)
    try:
        location = initialize.roomdict[inputint][3]
        rooms.append(location)
        #print(location)
        return location
    except:
        print("Room file not found.")
        return None
 
def whereami(string1, string2):
    inputstring = string1+string2
    inputint = int(inputstring)
    
    location = initialize.roomdict[inputint][0]
    return location

def getItem(obj):
  #Checks objects in the room against string "object", returns object
  x = utils.x
  y = utils.y
  where = library(str(x), str(y))
  items = __import__(where).itemshere
  for i in range(len(items)):
    if items[i].name == obj:
      return items[i]

def hasItem(obj):
    #Checks objects in the room against string "object"
  x = utils.x
  y = utils.y
  where = library(str(x), str(y))
  items = __import__(where).itemshere
  for i in range(len(items)):
    if items[i].name == obj:
      return True
  return False

def processLanguage(obj=None):        
    #basic variables
    validCommand = False
    noun = ""
    verb = ""
    command = input(" ")
    command = command.replace("'.,;:?[]{}|+-*&^%$#@!~_", "")
    splitCommand = command.split()
    x = utils.x
    y = utils.y
    where = library(str(x), str(y))
    
    #Check for non-empty input
    while len(splitCommand) == 0 or not validCommand:
        splitCommand = command.split()
        verb = splitCommand[0].lower()
        
        #1-word commands
        if len(splitCommand) == 1: 
            if (verb == "n") | (verb == "north"):
                __import__(where).movenorth()
                validCommand = True
            if (verb == "e") | (verb == "east"):
                __import__(where).moveeast()
                validCommand = True
            if (verb == "s") | (verb == "south"):
                __import__(where).movesouth()
                validCommand = True
            if (verb == "w") | (verb == "west"):
                __import__(where).movewest()
                validCommand = True
            if (verb == "look"):
                __import__(where).basicDes()
                validCommand = True
            if (verb == "cheat"):
                rooms.unlockRooms()
                validCommand = True
            if verb == "help":
                T.help()
                validCommand = True
  
        #2-word commands
        if len(splitCommand) >= 2:
            noun = splitCommand[1].lower()
            x = utils.x
            y = utils.y
            
            if command == "where am i":
                locate = whereami(str(x), str(y))
                print("You are currently in", locate, ".")
                validCommand = True
            noun = splitCommand[1].lower()
            if verb == "read":
                if 'userguide'== noun or 'guide' == noun:
                    T.readUserGuide()
                    validCommand = True                    

            if hasItem(noun):
                obj = getItem(noun)
                if (verb == "exam") | (verb == "examine"):
                    obj.examine()
                    validCommand = True
                if (verb == "take"):
                    obj.take()
                    validCommand = True
                if (verb == "use"):
                    obj.use()
                    validCommand = True
                if verb == "read" and ("paper" == obj.name or "note" == obj.name):
                    validCommand = True
                    obj.use()
                  
                    
        #3-word commands
        if len(splitCommand) == 3:
            if (verb == "read" or verb == "exam" or verb == "examine"):
                if splitCommand[1].lower() == "user's" and splitCommand[2].lower() == "guide":
                    T.readUserGuide()
                    validCommand = True
                if splitCommand[1].lower() == "sticky" and splitCommand[2].lower() == "notes":
                    print("The notes mostly contain sketches of strange robots and bizarre contraptions, surrounded by hearts")
                    validCommand = True
    
        #else
        if len(splitCommand) == 0 or not validCommand:
            print("Please input a valid command")
            command = input(" ")
            
# print("What should I do?")

while True:
    processLanguage()
    