import matplotlib.pyplot as plt
import shapely.geometry
import cv2
import numpy as np

def fillGaps(contours):
    '''
    When coincident fragments, split the contours
    '''
    resulting_contours = []
    '''
    contours = [
        np.array([[[70,70]],[[10,10]],[[20,10]],[[70,70]]], dtype=np.int32), 
        np.array([[[50,50]],[[11,10]],[[22,10]]], dtype=np.int32)
        #np.array([[[70,70]],[[10,10]],[[20,20]],[[30,30]][[70,70]],[[70,70]]], dtype=np.int32), 
        #np.array([[[50,50]],[[11,10]],[[21,20]],[[31,30]],[[50,50]]], dtype=np.int32),
    ]
    '''
    
    
    print("extractOverlappingContours over len(contours)= ",len(contours))
    for i in range(len(contours)):
        for j in range(i+1, len(contours)):
            print("comparing contour num "+str(i)+" with num"+str(j))
            print("*********************")
            c1 = contours[i]
            c2 = contours[j]
            '''
            if len(c1) >= len(c2):
                rc  = substractContours(c1, c2)
            else:
                rc  = substractContours(c2, c1)
            '''
            c1 = alignContours(c1, c2)
            contours[i] = c1
            resulting_contours.append([c1])#debug

            #print("resulting_contours=")
            #print(resulting_contours)
            '''
            rc  = substractContours(c2, c1)
            for c in rc:
                resulting_contours.append(rc)
            '''

    return contours#resulting_contours             

def substractContours(c1, c2):
    '''
    - Order does not matter
    - There can be more than one matching segments
    - Assumens there're only occurrence of each segment in on contour
    '''
    #print("c1=", c1)
    #print("c2=", c2)
    current_contour = np.array(None)
    new_contour = None
    final_contours = []
    idxc1 = 0
    idxc2 = 0
    overlapping = False
    while idxc1 < len(c1):
        #print("iter: idxc1="+str(idxc1)+", idxc2="+str(idxc2))
        print("\tc1[idxc1]="+str(c1[idxc1])+", c2[idxc2]="+str(c2[idxc2]))
        #print("check idxc1="+str(idxc1)+" vs "+str(idxc2))
        if np.array_equal(c1[idxc1], c2[idxc2]) and not overlapping:
        #if np.allclose(c1[idxc1], c2[idxc2], rtol=0.1) and not overlapping: 
        #if similarPoints(c1[idxc1], c2[idxc2]) and not overlapping: 
            print("start overlapping")
            print("\tc1[idxc1]="+str(c1[idxc1])+", c2[idxc2]="+str(c2[idxc2]))
            #guardem el contour previ (np.concatenate(a, axis=-1))
            #creem nou contour
            new_contour = np.empty((0,1,2), np.int32) #np.array(None)
            #afegim punt a un nou contour
            new_contour = np.concatenate((new_contour, [c1[idxc1]]), axis=0) #c1[idxc1])
            #new_contour = np.vstack((new_contour, [-3, -3])) 
            idxc1 = idxc1 + 1 
            overlapping = True              
        #elif np.array_equal(c1[idxc1], c2[idxc2]) and overlapping:
        #elif np.allclose(c1[idxc1], c2[idxc2], rtol=0.1) and overlapping:
        elif similarPoints(c1[idxc1], c2[idxc2]) and overlapping:
            print("continue overlapping")
            print("\tc1[idxc1]="+str(c1[idxc1])+", c2[idxc2]="+str(c2[idxc2]))
            #afegim punt a un nou contour
            new_contour = np.concatenate((new_contour, [c1[idxc1]]), axis=0)
            idxc1 = idxc1 + 1 
        elif not np.array_equal(c1[idxc1], c2[idxc2]) and overlapping:
            #print("stop overlapping")
            final_contours.append(new_contour)
            new_contour = None
            overlapping = False
            idxc2 = 0
            idxc1 = idxc1 + 1
        #else:
            #print("no coincidence")

        if idxc2 < len(c2)-1:
            idxc2 = idxc2 + 1
        else:
            if new_contour is not None:
                final_contours.append(new_contour)
                new_contour = None
            overlapping = False
            idxc2 = 0
            idxc1 = idxc1 + 1
    if new_contour is not None:
        final_contours.append(new_contour)
    #print(final_contours)    
    return final_contours

def similarPoints(p1, p2):
    #print("p1=", p1)
    #if abs(p1[0][0]-p2[0][0])+abs(p1[0][1]-p2[0][1]) <= 185:
    if euclideanDistance(p1, p2) <= 100:
        return True
    else:
        return False  

def euclideanDistance(p1, p2):
    d = np.sqrt(pow(p1[0][0]-p2[0][0], 2) + pow(p1[0][1]-p2[0][1], 2))
    #print("euclideanDistance("+str(p1)+", "+str(p2)+"="+str(d))
    #print("euclideanDistance(np.sqrt(("+str(p1[0][0])+"-"+str(p2[0][0])+")^2 + ("+str(p1[0][1])+"-"+str(p2[0][1])+")^2)")
    return d

     

def alignContours(c1, c2):
    #Make a copy of c1, the simliar points will be changed here to be equal to c2
    alignedC1 = np.copy(c1)
    #matchingPoints = np.empty((0,1,2), np.int32) 


    #For each point, find the closest. If it's enough close, use same value
    distances = np.zeros((len(c1), len(c2)))
    for idxc1 in range(len(c1)):
        for idxc2 in range(len(c2)):
            d = euclideanDistance(c1[idxc1], c2[idxc2])
            distances[idxc1][idxc2] = d
    #Sort distances from smallest to greatest
    distancesSorted = np.dstack(np.unravel_index(np.argsort(distances.ravel()), (len(c1), len(c2))))
    
    #Save the indices of the similar points found 
    assignedI = []
    assignedJ = []
    for k in range(len(distancesSorted[0])):
        i = distancesSorted[0][k][0]
        j = distancesSorted[0][k][1]
        if distances[i][j] < 10 and i not in assignedI and j not in assignedJ:
            if (distances[i][j]!=0):
                print("matching!")
            assignedI.append(i)
            assignedJ.append(j)
            alignedC1[i] = c2[j]
            #matchingPoints = np.concatenate((matchingPoints, [c2[j]]), axis=0)


    return alignedC1

        





