from player import Player
inventory = []

class Item:
    def __init__(self, name, unlocked, canTake, description, interactable, useText, unlockText):
        self.name = name
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

class Computer:
    def __init__(self, unlocked, description):
      self.name = "computer"
      self.unlocked = unlocked
      self.description = description

    def use(self):
      if self.unlocked == False:
        tryingPassword = True
        password = input("Please enter the password: \n")
        while (not self.unlocked) and tryingPassword:
            if password == "MEF19948":
                self.unlocked = True
                print("Welcome")
                self.home()
            elif password == "exit":
                tryingPassword = False
                print("I leave the computer")
            else: 
                password = input("Incorrect password. Please try again. Type 'exit' to leave the computer. \n")

    def examine(self):
        print(self.description)

    def home(self):
        print("The screen is covered in files, some of which are 'Ada', 'To do', and 'Spare Key'")
        file = (input("Which will you open?\n")).lower()
        filesplit = file.split()
        if filesplit[0] == "chmod":
            print("Ha, tricky! But no - not allowed")
            self.home()
        elif "ada" in file:
            print("ACCESS DENIED: It took me forever to get her working! I know I'll be tempted to make changes (and probably break her) so SHE'S LOCKED!")
            self.home()
      
        elif "to do" in file or "todo" in file:
            print("1. Check on AI project [reminder missed] \n2. Hide fun projects in office before Rin comes in from HQ and takes them again... I miss you, Rosie! [reminder snoozed] \n3. Find more things to put on to-do list [reminder missed]")
            self.home()
        elif "spare key" in file:
            print("Downloading spare key to nearest wireless device....")
            player.key1 = True
            print("Downloaded!")
            print("I have [name]'s key!'")
            print("I'm done with the computer, so I log off.")
        elif "exit" in file:
            print("I log off the computer.")
        else:
           print("That's not a valid command")
           self.home()


broom = Item("broom", True, True, "an ordinary broom", True, "I'm sweeping", "")
terminal1 = Item("terminal", True, False, "The terminal reads \n\'LOCKED\'", True, "It seems to require an NFC key", "You interact with the NFC terminal and the screen changes: \n\‘UNLOCKED\’")
terminal2 = Item("terminal", True, False, "The terminal reads \n\'LOCKED\'", True, "It seems to require an NFC key", "You interact with the NFC terminal and the screen changes: \n\‘UNLOCKED\’")
computer1 = Computer(False, "A fairly modern PC. Some sticky notes line the edges of the monitor. A keyboard sits in front of it on the desk.")
nullItem = Item("", False, False, "", False, "", "")
trash = Item("trash", True, False, "Inside the bin, there is a piece of paper.", True, "I could take the paper out of it", "")
paper = Item("paper", True, False, "It reads: April 20, 2020. Head of Robotics at [company], [name], has been awarded for remarkable contribution to science for her creation of a highly adaptable cleaning robot. At the age of 28, she is one of the youngest scientists to ever achieve such an acomplishment. We're excited to see what she does next.", True, "It reads: April 20, 2020. Head of Robotics at [company], [name], has been awarded for remarkable contribution to science for her creation of a highly adaptable cleaning robot. At the age of 28, she is one of the youngest scientists to ever achieve such an acomplishment. We're excited to see what she does next.", "")
keyboard = Item("keyboard", True, False, "A beat up old keyboard. There's a note sitcking out from under it.", True, "A beat up old keyboard. There's a note sitcking out from under it.", "")
note = Item("note", True, False, "It reads: 'If I forget again: Initials Birth year Lucky number, no spaces. PS: create a better password.'", True, "It reads: 'If I forget again: Initials Birth year Lucky number, no spaces. PS: create a better password.'", "")