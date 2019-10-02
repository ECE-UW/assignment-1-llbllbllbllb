"""

Name: Libang Liang
Student ID: 20662701
Email: l38liang@uwaterloo.ca
Electrical and Computer Engineering, University of Waterloo
a1ece650.py

"""
from __future__ import print_function
import sys
import re

import calculateGraph

#a "Libang Street" (1,2) (3,4) (5,6)
streetList = {}
# YOUR CODE GOES HERE

def main():
    ### YOUR MAIN CODE GOES HERE

    ### sample code to read from stdin.
    ### make sure to remove all spurious print statements as required
    ### by the assignment
    while True:
        try:
            line = raw_input()
            # if line != '\n':  # just hit enter will not check anything, prevent index out of range
            checkCommand(line)
        except EOFError:
            sys.exit()

    # for line in sys.stdin.readline():
    #     checkCommand(line)
    # sys.exit()

            # print 'read a line:', line

    #     except Exception as exp:
    #         print("Error: " + str(exp))
    # # return exit code 0 on successful termination
    # sys.exit(0)

def checkCommand(command):
    # remove all leading white space using .lstrip()
    # command = command.lstrip()

    if checkValid(command):
        if command[0] == 'a':  # add a street
            addStreet(command)

        elif command[0] == 'c':  # change a street
            changeStreet(command)

        elif command[0] == 'r':  # remove a street
            removeStreet(command)

        elif command[0] == 'g':  # produce output
            produceOutput()

    else:
        pass
        # print("Error: Your command is not valid, please type again", file=sys.stderr)

def addStreet(command):
    # print("enter add street function")
    streetName = re.findall('"([^"]*)"', command)   #list contains only one string
    lineSegment = re.findall('\(([^)]+)',command)   #list of strings
    coords = [map(int, i.split(',')) for i in lineSegment]  # Convert list of string to list of coordinates

    # Check if input is already in the list
    if streetName[0].lower() in [key.lower() for key in streetList.keys()]:     # Case insensitive
        print("Error: '" + streetName[0] + "' is already in the list! You can modify this street using 'c'")
    else:
        streetList[streetName[0]] = coords    #key is the street name, content is the line segment
        # print('Street successfully added!')

    # print('Current street list is shown below:\n')


def changeStreet(command):

    streetName = re.findall('"([^"]*)"', command)  # list contains only one string

    existNameList = streetList.keys()
    foundStreet = False

    for i in range(len(existNameList)):
        if streetName[0].lower() == existNameList[i].lower():
            foundStreet = True
            lineSegment = re.findall('\(([^)]+)', command)  # list of strings
            coords = [map(int, j.split(',')) for j in lineSegment]  # Convert list of string to list of coordinates
            streetList[existNameList[i]] = coords   # Replace the line segment with new input
    if foundStreet == False:
        print("Error: 'c' specified for a street that does not exist.")


def removeStreet(command):

    streetName = re.findall('"([^"]*)"', command)  # list contains only one string
    existNameList = streetList.keys()
    foundStreet = False

    for i in range(len(existNameList)):
        if streetName[0].lower() == existNameList[i].lower():
            foundStreet = True
            del streetList[existNameList[i]]   # Delete from Dictionary
            # print(str(streetList))
    if foundStreet == False:
        print("Error: 'r' specified for a street that does not exist.")

def produceOutput():
    vertexList, edgeList = calculateGraph.produceVertexOutput(streetList)

    # Produce vertex list string specified in assignment 1
    vertexOutputString = "V = {\n"
    for i in range(len(vertexList)):
        coordX = outputDecimalFormating(vertexList[i][0])
        coordY = outputDecimalFormating(vertexList[i][1])
        vertexOutputString += "  {:<4}({},{})\n".format(str(i+1)+":",coordX,coordY)
    vertexOutputString = vertexOutputString + "}"
    print(vertexOutputString)

    # Produce edge list string specified in assignment 1
    edgeOutputString = "E = {\n"
    for i in range(len(edgeList)):
        pointOne = edgeList[i][0]
        pointTwo = edgeList[i][1]
        edgeOutputString += "  <" + str(pointOne) + "," + str(pointTwo) + ">"
        if i < len(edgeList)-1:
            edgeOutputString +=  ",\n"
        else:
            edgeOutputString += "\n"
    edgeOutputString = edgeOutputString + "}"
    print(edgeOutputString)


def outputDecimalFormating(x):
    return '{0:.2f}'.format(x)
    # if isinstance(x,float):
    #     if x.is_integer():
    #         return str(int(x))
    #     else:
    #         return '{0:.2f}'.format(x)
    # else:
    #     return str(x)

def checkValid(command):

    if command == "":
        print("Error: Empty input, a: add street, c: change street, r: remove street, g: produce output")
        return False
    #for 'a' and 'c':
    if command[0] == 'a' or command[0] == 'c':
        pattern = re.compile("^[ac]\s\s*\"[A-Za-z ]+\"\s\s*(\([-]?[0-9]+,[-]?[0-9]+\)\s*){2,}$")
        result = pattern.match(command)
        if result != None: # Found correct command
            return True
        else:
            print("Error: In 'a' or 'c', Your command is not valid, please type again")
            return False

    # for 'r':
    elif command[0] == 'r':
        pattern = re.compile("^[r]\s\s*\"[a-zA-Z ]+\"\s*$") # ^: start of string, $: end of string
        result = pattern.match(command)
        if result != None:
            return True
        else:
            print("Error: In 'r', Your command is not valid, please type again")
            return False

    elif command[0] == 'g':
        pattern = re.compile("^[g]\s*$")
        result = pattern.match(command)
        if result != None:
            return True
        else:
            print("Error: In 'g', Your command is not valid, please type again")
            return False

    else:
        print("Error: Your command should start with 'a', 'c', 'r' or 'g', please type again")
        return False



def printStreetList():
    print(streetList)

if __name__ == '__main__':
    main()