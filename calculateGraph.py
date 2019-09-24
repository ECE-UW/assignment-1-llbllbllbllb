"""

Name: Libang Liang
Student ID: 20662701
Email: l38liang@uwaterloo.ca
Electrical and Computer Engineering, University of Waterloo
calculateGraph.py

"""
import calIntersection

# a = {'Weber Street':[[2,-1],[2,2],[5,5],[5,6],[3,8]],'King Street S':[[4,2],[4,8]],'Davenport Road':[[1,4],[5,8]]}
# a = {'Weber Street':[[2,1],[2,2]],'King Street S':[[4,2],[4,8]],'Davenport Road':[[1,4],[5,8]]}
# a = {'Weber Street':[[2,2],[5,5]],'Davenport Road':[[6,6],[7,7]]}

def calVertexAndEdge(a):

    vertex = []  # Output vertex
    vertexDict = {}  # OUtput vertex with index
    edge = []  # Output edge
    """
    intersectionList is to store intersections by line segment they are in. Used to find edges between intersections
    key will be the line segment index(street name + an integer),
    value will contain list of 1. line segment coordinates and 2. intersections
    """
    intersectionList = {}
    keyList = a.keys()
    for keyPt1 in range(len(keyList)):
        for keyPt2 in range(keyPt1 + 1, len(keyList)):
            currentSt1 = keyList[keyPt1]
            currentSt2 = keyList[keyPt2]

            for i in range(len(a[currentSt1]) - 1):
                for j in range(len(a[currentSt2]) - 1):

                    # Get line segments to calculate intersection
                    p1 = a[currentSt1][i]
                    p2 = a[currentSt1][i + 1]
                    q1 = a[currentSt2][j]
                    q2 = a[currentSt2][j + 1]

                    currentLineSegment1 = currentSt1 + str(i)
                    currentLineSegment2 = currentSt2 + str(j)


                    # Calculate intersection
                    intersection = calIntersection.calIntersect(p1[0], p1[1], p2[0], p2[1], q1[0], q1[1], q2[0], q2[1])

                    # Check and add points to vertex
                    if intersection != None:

                        # Add to vertex
                        for noOfIntersection in range(len(intersection)):
                            if intersection[noOfIntersection] not in vertex:
                                vertex.append(intersection[noOfIntersection])

                        if p1 not in vertex:
                            vertex.append(p1)
                        if p2 not in vertex:
                            vertex.append(p2)
                        if q1 not in vertex:
                            vertex.append(q1)
                        if q2 not in vertex:
                            vertex.append(q2)

                        # Add intersection to dict to calculate edges
                        addToIntersectionDict(intersectionList,currentLineSegment1, currentLineSegment2, intersection, p1, p2, q1, q2)


    # Add index to vertex after done
    for i in range(0,len(vertex)):
        vertexDict[i+1] = tuple(vertex[i])


    # Calculate edge
    calEdge(intersectionList,edge,vertexDict)
    return vertex,edge




def addToIntersectionDict(intersectionList,lineSegName1, lineSegName2, intersection, p1, p2, q1, q2):
    # This function is to gather line segments that contain intersection. For later use of edge computation

    if lineSegName1 in intersectionList:
        # Intersection list for this line segment already exist, append intersection to value
        for i in range(len(intersection)):
            if intersection[i] not in intersectionList[lineSegName1]:
                intersectionList[lineSegName1].append(intersection[i])
            else:
                pass
    else:
        # Line segment not exist, add new one
        intersectionList[lineSegName1] = [p1,p2]
        for i in range(len(intersection)):
            intersectionList[lineSegName1].append(intersection[i])



    if lineSegName2 in intersectionList:
        # Intersection list for this line segment already exist, append intersection to value
        for i in range(len(intersection)):
            if intersection[i] not in intersectionList[lineSegName2]:
                intersectionList[lineSegName2].append(intersection[i])
            else:
                pass
    else:
        # Line segment not exist, add new one
        intersectionList[lineSegName2] = [q1,q2]
        for i in range(len(intersection)):
            intersectionList[lineSegName2].append(intersection[i])

    # print(intersectionList)

def calEdge(intersectionList,edge,vertexDict):
    # This function is to calculate edge output base on intersectionList calculated before

    intersectionSegNameList = intersectionList.keys()

    for i in range(len(intersectionSegNameList)):
        intersectionSegName = intersectionSegNameList[i]


        coordsList = intersectionList[intersectionSegName]
        removeDuplicateList = []
        # there may be same point that are stored twice, for example an end point itself is a intersection point
        # the following for loop removes those duplicate point
        for element in coordsList:
            if element not in removeDuplicateList:
                removeDuplicateList.append(element)

        # rearrange the list such that x,y in ascending order
        # which means coordinates are in order from left to right, bottom to up,
        # so each neighbouring point in the list are also neighbouring point on the graph
        sortedCoordsList = sorted(removeDuplicateList, key=lambda k: [k[0], k[1]])
        # print(sortedCoordsList)
        # Loop through sorted coordinate list to find corresponding index
        for j in range(len(sortedCoordsList)-1):
            vertexID1 = vertexDict.keys()[vertexDict.values().index(tuple(sortedCoordsList[j]))]
            vertexID2 = vertexDict.keys()[vertexDict.values().index(tuple(sortedCoordsList[j+1]))]
            # print("vertexID1: " + str(vertexID1) + " vertexID2: " + str(vertexID2))
            # print("edge: " + str(edge))
            checkOne = [vertexID1,vertexID2]
            checkTwo = [vertexID2,vertexID1]
            if checkOne not in edge:
                if checkTwo not in edge:
                    edge.append([vertexID1,vertexID2])



    #sorted(a, key=lambda k:[k[0],k[1]])
    #key by value

def produceVertexOutput(streetList):
    # Clear previous vertex and edge information

    vertex,edge = calVertexAndEdge(streetList)
    return vertex,edge
    # also need to print edge



