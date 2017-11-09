import random
import Face #.py file containing the object constructor and methods for a face of the cube
def getRow(face, row): #Returns a string with every character in that row of that side of the cube
    """Returns string of each character in the list. Parameters are a side object: face, and an int row"""
    temp = ""
    for x in xrange(3): #Steps through row
        temp += face.yRow[row][x] +" " #Adds character to the temp string with a space
    return temp #Returns the string
def build(): #Builds each face of the cube
    center = Face.side('W') #Each face is given a color and a name
    left = Face.side('G') #Names are based on their relative starting positions
    right = Face.side('Y') #W: White, G: Green, Y: Yellow, B: Blue, R: Red, O: Orange
    back = Face.side('B')
    bottom = Face.side('R')
    top = Face.side('O')
    center.alterNeighbor(left, right, top, bottom) #Tells each side of the cube who their bordering neighbors are
    left.alterNeighbor(back, center, top, bottom) #The order they are inserted in is how they are related
    right.alterNeighbor(center, back, top, bottom) #Position 0: left, 1: right, 2: top, 3: bottom 
    back.alterNeighbor(right, left, bottom, top)
    bottom.alterNeighbor(left, right, center, back)
    top.alterNeighbor(left, right, back, center)
    return center #Returns the center face (to be set to the current center later on)
def display(): #Draws the faces of the cube on screen. Not pretty, but it works.
    """Prints every character in every row of every side object, relative to the current center. Ends by querying the user for a command."""
    print("         " + "TOP" + "        \n") #Labels sit above each face
    for x in xrange(3): #For each column
        print("         " + getRow(current.getTarget(2), x) + "         \n") #Print each row of the cube above the current center
    print("LEFT     " + "CENTER" + "    RIGHT\n")
    for x in xrange(3): #Prints rows for the left face, current center, and right
          print(getRow(current.getTarget(0), x) + "     " + getRow(current, x) + "   " + getRow(current.getTarget(1), x) +"\n")
    print("         " + "BOTTOM" + "            \n")
    for x in xrange(3):
        print("         " + getRow(current.getTarget(3), x) + "         \n")
    print("         " + "BACK" + "        \n")
    for x in xrange(3):
        print("         " + getRow(current.getTarget(3).getTarget(3), x) + "         \n")
    print("\n\n Enter command: r (rotate), c (recenter), m (mixup), q (quit)")#Asks user for command
    
def getCommand(): #Determines what the user wants to do
    """Gets text input from the user to determine what command to perform"""
    inp = raw_input().lower() #Takes in lower case input from the shell
    if(inp == 'r'): #If they entered an r
        spin() #rotate a row or column using the spin function
    elif(inp == 'c'): #If they entered a c
        recenter() #Re-center the cube on a different face
    elif(inp == 'm'): #If they entered an m
        mixup() #Mix up the cube with the mixup function
    elif(inp == 'q'): #If they entered a q
        return 0 #Signal the main method to quit
    else: #If they entered none of those
        print("Please enter a single letter command!\n r (rotate), c (recenter), m (mixup), q (quit)")
        getCommand() #Ask again
    return 1 #Return a 1 if they did not quit

def direct(): #Determines which direction the user will rotate the given row or column
    """Gets text input from the user to determine which direction to act on a row or column"""
    print("\n\n Please enter the direction you would like to rotate: U(up), L (left), R (right), D(down)")
    inp = raw_input().lower() #Takes in lower case input
    if(inp == 'u'): #Up
        return 2
    elif(inp == 'l'): #Left
        return 0
    elif(inp == 'r'): #Right
        return 1
    elif(inp == 'd'): #Down
        return 3
    else:
        print("\n Invalid command") #Neither?
        return direct() #Ask again

def spin(): #This manages the rotation of the row or column
    """Uses helper functions to determine row/column and direction of a move, and orders the sides of the cube to do it."""
    temp = direct() #Determines the direction with the direct function
    if(temp < 2): #If it is going left or right
        x = row("row") #If must be a row, determine which with the row function
    else: #Otherwise it must be up or down
        x = row("column") #Determine which column with the row function
    current.move(x, 0, temp) #Start the rotation process with the current center, based on the inputs from user
def row(thing):#Determines which row or column is moving, with a string for either row or column passed in
    """Gets text input from the user to determine which row or column to act on. String thing determines if it is a row or column."""
    print("\n\n Please select which "+ thing +" you would like to rotate! (1-3)")
    inp = raw_input() #Retrieves an input from user
    try: #Tries to
        x = int(inp) #Convert that to an int
    except ValueError: #If it can't
        x=4 #Set the input value to an invalid number
    if(x < 4 and x > 0): #If the value is kosher
        return x-1 #Return it -1 (offset for the 0th index position)
    else: #Otherwise
        print("\n Please enter a valid number!")
        return row() #Ask again
def recenter():#Allows the user to set a different face to be the center
    """Re-centers the draw sides of the cube around a different face."""
    print("\n\n Please enter which face you would like to center on: L (left), R (right), T (top), BT (bottom), B (back)")
    inp = raw_input().lower() #Determines which face the user would like to center on
    global current #All relative to the global current, a side object representing the current center
    if(inp == 'l'): #If they chose left
        current.getTarget(2).rotate() #Rotate the top
        current.getTarget(3).rotate() #And bottom relative sides so they act as though the cube was just turned
        current = current.getTarget(0) #Set left to be the new current center
    elif(inp == 'r'): #Right works identical to left
        current.getTarget(2).rotate()
        current.getTarget(3).rotate()
        current = current.getTarget(1)
    elif(inp == 't'):#If they chose top
        current.getTarget(0).rotate() #The left and right relative sides
        current.getTarget(1).rotate() #Must rotate
        current = current.getTarget(2)#Top is the new current center
    elif(inp == 'bt'): #Bottom works the same as top
        current.getTarget(0).rotate()
        current.getTarget(1).rotate()
        current = current.getTarget(3)
    elif(inp == 'b'): #If they chose the back face, nothing needs to rotate, only the current needs to be updated
        current = current.getTarget(1).getTarget(1) #Then get the back through the right side of the right side
    elif(inp == 'c'): #If they chose the current center
        return #Just exit the function
    else: #If they entered none of those
        print("\n Please enter valid face")
        recenter() #Ask again
def mixup(): #Function to automatically mixup the cube for the player to solve
    """Automatically mixes up the cube using random numbers"""
    global current #Uses the global current, a side object from the Face package
    loops = random.randrange(5,25) #Picks a random number of moves (between 5 and 25)
    while(loops > 0): #While it still has moves left
        if(random.randrange(1,2) == 1): #Randomly choose between rotating a row/column and re-centering
            current.move(random.randrange(0,2), -1*int(random.randrange(0,16,4)), random.randrange(0,3))
            #Randomly picks a row/column to move, how many times to spin it (between 1 and 4), and whicch direction
        else: #If it chooses to change the center face
            t = random.randrange(0,3) #Pick a random direction to re-center on
            if(t < 2): #If it is left or right
                r = 2 #Then it is the top that needs to rotate first
            else: #If it is top or bottom
                r = 0 #It is left that needs to rotate first
            current.getTarget(r).rotate() #Rotates the designated face
            current.getTarget(r+1).rotate() #Rotates the next one (bottom or right)
            current = current.getTarget(t) #Sets the new current center to the chosen face
        loops -= 1 #Ends that turn
def main(): #Main loop
    """Loops the program as long as the user doesn't enter the quit command."""
    quiter = 1 #If they don't wish to quit yet it is  1
    while(quiter == 1):  #While they don't want to quit
        display() #Display the current cube
        quiter = getCommand() #Get inputs and watch to see if they quit
current = build() #Sets global current to be the returned center from the newly built faces
main() #Runs the main functions loop
