"""

Name: Libang Liang
Student ID: 20662701
Email: l38liang@uwaterloo.ca
Electrical and Computer Engineering, University of Waterloo
calIntersection.py

"""
def calIntersect(p1_x,p1_y,p2_x,p2_y,q1_x,q1_y,q2_x,q2_y):

    r_x = p2_x - p1_x
    r_y = p2_y - p1_y

    s_x = q2_x - q1_x
    s_y = q2_y - q1_y

    divider =  crossProduct(r_x,r_y,s_x,s_y)    # r.s
    t_nominator = crossProduct(q1_x - p1_x, q1_y - p1_y, s_x, s_y)  #(q-p).s
    u_nominator = crossProduct(q1_x - p1_x, q1_y - p1_y, r_x, r_y)  #(q-p).r

    if divider != 0:

        t = float(t_nominator) / float(divider)
        u = float(u_nominator) / float(divider)

        if t>=0 and t<=1 and u>=0 and u<=1:
            # Intersection found
            crossPoint_x = p1_x + t*r_x
            crossPoint_y = p1_y + t*r_y
            return([[crossPoint_x,crossPoint_y]])

        else:
            # Not parallel, not intersect, return nothing
            return None

    else:
        if u_nominator == 0:
            #colinear need to investigate
            t0 = (dotProduct(q1_x-p1_x,q1_y-p1_y,r_x,r_y))/(dotProduct(r_x,r_y,r_x,r_y))
            t1 = t0 + (dotProduct(s_x,s_y,r_x,r_y))/(dotProduct(r_x,r_y,r_x,r_y))

            SdotR = dotProduct(s_x,s_y,r_x,r_y)
            # print("s.r = " + str(SdotR))


            pointList = []
            if SdotR >= 0:
                # compare [t0,t1]
                if (t1<0 and t0<t1) or (t0>1 and t1>t0): # Not intersect [0,1]
                    # No intersection
                    pass
                else:
                    # Find intersection
                    # Intersection would be coordinate(s) in the middle
                    conllinearList = [[p1_x,p1_y],[p2_x,p2_y],[q1_x,q1_y],[q2_x,q2_y]]
                    removeDuplicateList = []
                    for element in conllinearList: # Remove duplicate
                        if element not in removeDuplicateList:
                            removeDuplicateList.append(element)
                    sortedCoordsList = sorted(removeDuplicateList, key=lambda k: [k[0], k[1]])
                    pointList = sortedCoordsList[1:-1] # remove first and last element




            else:
                # compare [t1,t0]
                if (t0<0 and t1<t0) or (t1>1 and t0>t1): # Not intersect [0,1]
                    pass
                else:
                    # Find intersection
                    # Intersection would be coordinate(s) in the middle
                    conllinearList = [[p1_x, p1_y], [p2_x, p2_y], [q1_x, q1_y], [q2_x, q2_y]]
                    removeDuplicateList = []
                    for element in conllinearList: # Remove duplicate
                        if element not in removeDuplicateList:
                            removeDuplicateList.append(element)
                    sortedCoordsList = sorted(removeDuplicateList, key=lambda k: [k[0], k[1]])
                    pointList = sortedCoordsList[1:-1] # remove first and last element


            if len(pointList) == 0: # No intersection
                return None
            else:   # One or two intersection(s)
                # print("t0 = " + str(t0) + " t1 = " + str(t1))
                # print("intersections: " + str(pointList))
                return(pointList)

        else:
            # Parallel but not intersect return nothing
            return None


def crossProduct(p_x,p_y,q_x,q_y):
    return p_x * q_y - q_x * p_y

def dotProduct(p_x,p_y,q_x,q_y):
    return float(p_x * q_x + p_y * q_y)
