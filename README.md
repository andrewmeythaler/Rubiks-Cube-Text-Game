# Rubiks-Cube-Text-Game
A text based game simulating a Rubik's Cube, made in Python.

It isn't pretty, but it works. There are three files that make it work: <a href="https://github.com/andrewmeythaler/Rubiks-Cube-Text-Game/blob/master/Face.py">Face.py</a>, the Python file containing the class representing each side or face of the cube. Face.pyc, the compiled package that Rubiks.py uses to run. And lastly, <a href="https://github.com/andrewmeythaler/Rubiks-Cube-Text-Game/blob/master/Rubiks.py">Rubiks.py</a>, the main program and associated functions.

# Face.py
Contains the code for the class 'side', representing one side, or face, of the Rubik's cube. Contained within each is a list yRow, holding 3 lists of characters. Each list inside representing one row of the Rubik's cube on that side. It also contains a list of other side objects, 'neighbors'. Inserted in order it contains a pointer to the adjacent sides on the left (0), right (1), top (2), and bottom (3).
### __init__(self, color)
This is the constructor method for the class. It takes self (supplied automatically by Python), and a char 'color' as parameters. Color is then used by the constructor to fill all of the characters in each character list, in the self.yRow list, to be that character (The color will either be G, green, Y, yellow, B, blue, R, red, O, orange, or W, white).
### getTarget(self, direction)
This is a method that returns a pointer to a side object, representing the neighboring face in that direction. The direction parameter is an integer designating where in the neighbor list to find the side object. 0 is left, 1 is right, 2 is top, 3 is bottom.
### move(self, row, count, direction)
This is a method that rotates the given row around the cube, to the neighboring faces. The row parameter is a numerical value representing the row (or column!) that is being moved. Count is an int that designates how many times around it is going (0 would move it to the adjacent face, -4 would be one more over, etc). Direction is an int that determines which direction it is rotating (0 and 1, left and right, operate differently than 2 and 3, top and bottom). This is then passed into <a href="gettargetself-direction">getTarget()<a> to get a pointer to the neighbor. Moving left or right is easy, simply storing the whole list for that row in a temp holder, telling each other face to do the same, and then once it has come all the way back around (determined by iterating count) the temp list is pushed to the adjacent side. Moving up or down is harder, requiring you to step through the yRow list and get individual characters in the column position of each char list, since columns don't actually exist in this class.
### alterNeighbor(self, left, right, top, bottom)
This method inserts the supplied pointers to adjacent faces into the neighbors list of sides. The parameters are pretty self explanatory and are inserted in order according to their position. 0th index being left, 1 being right, 2 being top, 3 being bottom.
### rotate(self)
This method rotates the side horizontally, so that when a different face is made the center, the relationship between adjacent sides still holds up. It takes no parameters other than the automatically supplied self. It creates a temp list of char lists, and starts filling it with values being fetched in reverse order from the yRow list. Then it sets the yRow list to be that temp list.

# Rubiks.py
This holds the main program, and it's associated functions. Originally I planned on making most functions in their own python file, but it caused problems with the global variable 'current' (representing whichever side is currently the center). Imports random (python library package for randomly generating numbers), and Face, the python file for the side class.
### getRow(face, row)
This function returns a string of every single character in a given row (supplied by the int row argument) of a given face (supplied by the face argument). Adds a space inbetween each letter to help it display better.
### build()
This function instantiates side objects for every single side of the Rubik's cube. It then uses the <a href="#alterneighborself-left-right-top-bottom">alterNeighbor()</a> function of each to supply them with points to adjacent faces. It then returns the side object it calls center, which will in the main program set it to be the global current object, making all other functions treat it as the center.
### display()
This function draws each side in order, relative to the current center side. First the top is drawn, on it's own row (offset by tabs for this effect). Then left, center, right on a row. Then bottom on it's own row. Then the back side of the cube is off at the very bottom. Text labels above each are also printed. The function ends by asking the user what <a href="#getcommand">command</a> they would like to enter (their input will be done in another function).
### getCommand()
This function gets the raw_input() from the user, and sets it to lower case. This (allegedly) single character should correlate to a command, if it does not, they are simply asked again. Commands are <a href="#spin">rotate (r)<a>, <a href="#receneter">re-center (c)</a>, <a href="#mixup">mixup (m)<a>, and <a href="#main">quit (q)</a>. If rotate, re-center, or mixup are selected, the appropriate functions are called. If quit is selected, the function returns a 0, indicating to the <a href="#main">main function</a> that the user wished to quit. If the other commands are executed properly, a 1 is returned, indictating to the <a href="#main">main function</a> that they do not wish to quit.
### spin()
Ths function oversees how a row or column is rotated, by retreiving commands from the user for which row or column is being moved and in what direction. First the direction is determined with the <a href="#direct">direct()</a> function. Then with that int value it determines if the user is moving left/right or up/down. If it is left or right it uses the <a href="#row">row()</a> function to determine which row is being moved (while passing in the string "row" so the text prompt within sounds correct). Otherwise it uses the row function to determine which column is being moved while passing in the string "column"). Then it takes both the direction, and the row/column, and uses the <a href="#moveself-row-count-direction">.move()</a> method in the current object, to get the whole rotation started (a 0 is passed in for count, indicating it only needs to rotate once).
### direct()
This function function determines which direction the user wishes to rotate any given row or column, based on the raw_input (also converted to lower case). The commands are left (l), right (r), up (u), or down (d). If an input is given that does not match, they are asked again. Otherwise an integer is returned, representing the index in any side's neighbors list that the pointer to that directional neighbor can be found.
### row(thing)
This function determines which row or column is being rotated. This function is not concerned with the difference between the row or column, and simply asks the user for a numerical value representing either. The thing parameter is a string that will fill in the text prompt with either "row" or "column" so the user knows what they are selecting. Using raw_input() converted to an integer, it looks to see if the users wants to move row/column 1, 2, or 3. If the user does not enter one of those values (or enters a non-integer!) it will simply ask again. After the user determines which one they want to select, the function returns that number, minus 1, so it corresponds to the index for that row/column.
### recenter()
This function is used to change which side object currently represents the center face. It asks the user which one they would like to center on, and then gets their answer with a raw_input() converted to lower case. The possible choices are left (l), right (r), top (t), bottom (bt), or back (b). These choices are of course relative to the current center. If the user enters something that is not one of those choices, it asks again. If they enter the secret option c (center) it simply returns a null value, ending the function. Once a side has been selected, the function determines which sides need to be <a href="#rotateself">rotated</a> to ensure spacial relationships don't break. If the left or right is selected to be centered on, the top and bottom must rotate. Conversely if the top or bottom is selected, left and right must rotate. The back however, is easy. Simply setting it to be the new center is sufficient, as the <a href="#display">display()</a> function will mirror left and right for you, already taking into account the flip.
### mixup()
This function is use to mixup up the cube for you, using a random set of random moves. First it determines how many random moves it will make (between 5 and 25 moves). Then it will randomly determine if it wants to use that move to A) rotate a row/column, or B) re-center on a different face. Rotating the face works similarly to the <a href="#spin>spin()</a> function, but using random numbers instead of user supplied values. This may change at a later time, to make spin more versatile and use supplied arguments instead of user input. Re-center similarly works on the same principles of re-center. But taking better advantage of the numerical relationships between the indices of sides that need to <a href="#rotateself">rotate<a>, and the sides being centered on.
### main()
This function is the main loop for the program. The only line of code not a part of this loop is the line that uses the <a href="#build">build()<a> function to set the global current, the side object for the center. Main will continue to loop through <a href="#display">displaying</a> the cube, and asking for commands, as long as the <a href="getcommand">getCommand()</a> function does not return a 0, indicating the user wishes to quit.
