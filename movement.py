x=0
y=0
position = [x,y]

def right():
    global position
    global x
    x = x+1
    position = [x,y]
    print(position)

def left():
    global position
    global x
    x = x-1
    position = [x,y]
    print(position)

def up():
    global position
    global y
    y = y+1
    position = [x,y]
    print(position)

def down():
    global position
    global y
    y = y-1
    position = [x,y]
    print(position)

while (True):
    value = input("Please Move:\n")
    if (value == 'n' or value == 'N'):
        up()
    elif (value == 's' or value == 'S'):
        down()
    elif (value == 'e' or value == 'E'):
        right()
    elif (value == 'w' or value == 'W'):
        left()
    else:
        print("Please type in either 'n', 's', 'e', or 'w':")