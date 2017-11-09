class side:
    """This class is for a single side of the rubix cube"""
    #green, yellow, blue, white, red, orange
    def __init__(self, color): #Constructor
        self.yRow = [['W','W','W'],['W','W','W'],['W','W','W']] #Local list of lists, yRow itself being the columns, each list within a row
        self.neighbors = [] #To keep track of which sides border it
        for y in self.yRow:
            for x in xrange(3):
                y[x] = color #Sets every tile on this face to the given color
    def getTarget(self, direction): #Returns a pointer to the side in a given direction
        return self.neighbors[direction] #0: left, 1: right, 2: up, 3: down
    def move(self, row, count, direction): #rotates the column or row
        target = self.getTarget(direction) #Determins where the tile is going
        count = count+1 #Makes sure we don't over-rotate
        if(direction < 2): #If we are going side to side (l or r)
            temp = self.yRow[row]#Dump the whole row in a temporary holder
            if(count < 5): #If this is not the last rotate
                target.move(row, count, direction) #Make sure the target side is also rotating it's row
            target.yRow[row] = temp #Then make sure everyone sets the adjacent row to the temp    
        elif(direction < 4): #If going up or down
            holder = [] #Hold will temporarily store all the characters in a given column (columns technically do not exist!)
            for y in self.yRow: #For every list of characters inside the list of lists
                holder.append(y[row]) #Take the character from the [ROW] column and put it in holder
            if(count < 5): #If it is not the last rotation
                target.move(row, count, direction) #Make sure the target side also rotates
            for x in xrange(3): #For every slot in the target column (3)
                target.yRow[x][row] = holder.pop(0) #Take the top character from self and put it in the correct slot of every target column
        else: #If it is going neither up nor down
            return #Just bail, something is wrong
    def alterNeighbor(self, left, right, top, bottom): #Sets the neighboring faces
        self.neighbors.append(left)
        self.neighbors.append(right)
        self.neighbors.append(top)
        self.neighbors.append(bottom)
    def rotate(self): #Rotates the given side if the player decides to center on another face, turning the whole 'cube'
        temp = [['X','X','X'],['X','X','X'],['X','X','X']] #create a temp list of lists of chars
        for y in xrange(3): #For every column
            for x in xrange(3): #And every row in those columns
                temp[y][x] = self.yRow[2-x][2-y] #Make temp be that tile, counting backwards on yRow
        self.yRow = temp #Set yRow to temp (doing it in reverse order causes problems as it just makes temp a pointer to yRow)
