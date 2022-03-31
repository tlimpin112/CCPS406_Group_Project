inventory = []
rooms = []
objects = []

class Player(object):
  def __init__(self):
    self.x = 5
    self.y = 5
    self.GPS = False
    
  def moveNorth(self, rooms):
    if rooms[self.x][self.y].northDoor:
      if not rooms[self.x][self.y + 1].locked:
        self.y = self.y + 1
        print(rooms[self.x][self.y].name)
      else: print("I can't go that way yet")
    else: print("There's no door that way")

  def moveEast(self, rooms):
    if rooms[self.x][self.y].eastDoor:
      if not rooms[self.x + 1][self.y].locked:
        self.x = self.x + 1
        print(rooms[self.x][self.y].name)
      else: print("I can't go that way yet")
    else: print("There's no door that way")

  def moveSouth(self, rooms):
    if rooms[self.x][self.y].southDoor:
      if not rooms[self.x][self.y - 1].locked:
        self.y = self.y - 1
        print(rooms[self.x][self.y].name)
      else: print("I can't go that way yet")
    else: print("There's no door that way")

  def moveWest(self, rooms):
    if rooms[self.x][self.y].westDoor:
      if not rooms[self.x - 1 ][self.y].locked:
        self.x = self.x - 1
        print(rooms[self.x][self.y].name)
      else: 
        print("I can't go that way yet")
        print(rooms[self.x - 1 ][self.y].name , " is locked: ", rooms[self.x - 1 ][self.y].locked)
    else: print("There's no door that way")

class Item(object):
  def __init__(self, unlocked, canTake, description, interactable, useText):
    self.unlocked = unlocked
    self.canTake = canTake
    self.inInventory = False
    self.description = description
    self.interactable = interactable
    self.useText = useText

  def unlock(self):
    self.unlocked = True

  def take(self):
    if self.canTake:
      self.inInventory = True
      inventory.append(self)
      print("I picked up the broom")
    else:
      print("I can't do that.")

  def examine(self):
    print(self.description)

  def use(self):
    if self.interactable:
      print(self.useText)
    else:
      print("I can't do anything with this")

    
    

class Room(object):
  def __init__(self, objects, NPC, northDoor, eastDoor, southDoor, westDoor, locked, name, description):
    self.objects = objects
    self.NPC = NPC
    self.northDoor = northDoor
    self.eastDoor = eastDoor
    self.southDoor = southDoor
    self.westDoor = westDoor
    self.locked = locked
    self.name = name
    self.description = description

  def look(self):
    print(self.description)

  def unlock(self):
    self.locked = False


player = Player()


broom = Item(True, True, "an ordinary broom", True, "I'm sweeping")
computer1 = Item(True, False, "A fairly modern PC. Some sticky notes line the edges of the monitor. A keyboard sits in front of it on the desk.", True, "I use the computer")


def loadRooms():

  noRoom = Room(False, False, False, False, False, False, True, "no room here", "void")
  origami = Room(False, False, True, False, False, False, True, "The Office of the Head of Origami Bots", "tbd")
  security = Room(False, False, True, False, False, False, True, "Security Office", "tbd")
  exit = Room(False, False, True, False, False, False, True, "The Exit", "The ultimate goal")
  server = Room(False, False, False, True, False, False, False, "Server room", "tbd")
  hall4 = Room(False, False, True, True, True, True, False, "Hallway", "tbd")
  hall5 = Room(False, False, False, True, True, True, False, "Hallway", "tbd")
  hall6 = Room(False, False, True, False, True, True, False, "Hallway", "tbd")
  construction = Room(False, False, False, False, False, True, True, "The Office of the Head of Contruction Bots", "tbd")
  storage = Room(False, False, False, False, True, False, False, "Storage room", "There's a lost and found box full of odd hats and coats")
  hall3 = Room(False, False, True, True, True, True, False, "Hallway", "tbd")
  creator = Room(False, False, False, True, False, False, False, "Creator's Office", "tbd")
  printing = Room(False, False, False, True, False, False, False, "3D Printing Lab", "tbd")
  hall2 = Room(False, False, True, True, True, True, False, "Hallway", "tbd")
  programming = Room(False, False, False, False, False, True, False, "Programming Lab", "tbd")
  outS = Room(False, False, True, True, False, False, False, "Outside space between the storage building and main lab", "tbd")
  oriStorage = Room(False, False, False, False, False, True, True, "Storage for Origami Bots", "tbd")
  proto = Room(False, False, False, True, False, False, False, "The Prototyping Lab", "tbd")
  hall1 = Room(False, False, True, True, True, True, True, "Hallway", "tbd")
  entrance = Room(False, False, False, True, False, True, False, "The building's side entrance", "tbd")
  outM = Room(False, False, True, True, True, True, False, "Outside space between the storage building and main lab", "tbd")
  consStorage = Room(False, False, False, False, False, True, True, "Storage for Contruction Bots", "tbd")
  obstacle = Room(False, False, False, True, False, False, True, "An obstacle course for testing robots", "tbd")
  testing = Room(False, False, False, False, True, True, False, "A lab for testing robots", "tbd")
  greenspace = Room(False, False, False, True, False, False, False, "An outdoor greenspace", "tbd")
  outN = Room(False, False, False, True, True, True, False, "Outside space between the storage building and main lab", "tbd")
  cleanStorage = Room(broom, False, False, True, False, True, True, "Storage for Cleaning Bots", "tbd")
  workshop = Room(computer1, False, False, False, False, True, False, "Someone's private workshop", "A small room with a computer on a desk")
  
  rooms.append([noRoom, server, creator, printing, proto, obstacle])
  rooms.append([origami, hall4, hall3, hall2, hall1, testing])
  rooms.append([security, hall5, construction, programming, entrance, greenspace])
  rooms.append([exit, hall6, storage, outS, outM, outN])
  rooms.append([noRoom, noRoom, noRoom, oriStorage, consStorage, cleanStorage])
  rooms.append([noRoom, noRoom, noRoom, noRoom, noRoom, workshop])
  

def unlockRooms():
  #Cheat to unlock all rooms
  for i in range(0, 6):
    for j in range(0, 6):
      if not (rooms[i][j].name == "no room here"):
        rooms[i][j].unlock()
      
def processLanguage():
  #basic variables
  validCommand = False
  noun = ""
  verb = ""
  command = input(" ")
  splitCommand = command.split()

  #Check for non-empty input
  while len(splitCommand) == 0:
    command = input("Please input a valid command")
    splitCommand = command.split()
  verb = splitCommand[0]
  if len(splitCommand) == 1:
    
    #1-word commands
    if (verb.lower() == "n") | (verb.lower == "north"):
      player.moveNorth(rooms)
      validCommand = True
    if (verb.lower() == "e") | (verb.lower == "east"):
      player.moveEast(rooms)
      validCommand = True
    if (verb.lower() == "s") | (verb.lower == "south"):
      player.moveSouth(rooms)
      validCommand = True
    if (verb.lower() == "w") | (verb.lower == "west"):
      player.moveWest(rooms)
      validCommand = True
  
    if (verb.lower() == "look"):
      rooms[player.x][player.y].look()
      validCommand = True
  
    if (verb.lower() == "cheat"):
      unlockRooms()
      validCommand = True

  #2-word commands
  if len(splitCommand) == 2:
    noun = splitCommand[1]
    if (verb.lower() == "exam") | (verb.lower() == "examine"):
      #Check that noun is a valid object
      if noun.lower() == "broom":
        broom.examine()
        validCommand = True
      if noun.lower() == "computer":
        computer1.examine()
        validCommand = True
  
    if (verb.lower() == "take") & (noun.lower() == "broom"):
      #Check that noun is a valid object
      broom.take()
      validCommand = True
  
    if (verb.lower() == "use"):
      if (noun.lower() == "broom"):
        broom.use()
        validCommand = True
      if (noun.lower() == "computer"):
        computer1.use()
        validCommand = True

  if not validCommand:
    command = input("Please input a valid command")




loadRooms()

print("I'm in", rooms[player.x][player.y].name ,". \n Write a command")
while True:
  processLanguage()