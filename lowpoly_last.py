import matplotlib.pyplot as plt
import shapely.geometry
import cv2
import numpy as np
import util_contours
import os
import traceback
import facial_landmarks
import sys

DRAW_CONTOURS_SIMPLIFIED=False
PRINT_COLOR_IDS=False

#WARNING: OpenCV colors are BGR!!!!


#NOTHING: (0, 255, 0)
#SKIN: (121,141,205,255)
#TSHIRT: (49,32,46,255)
#ORANGE HAIR: (5,56,182,255)
#TROUSERS: (34,34,34,255)
#BALL: (89,69,4,255)
color_assignmentNEW = {
    0: (255,0,255,255), #background (purple)
    1: (255,200,255,255), #pink
    2: (0,0,255,255),#red
    3: (0,0,255,255),
    4: (0,0,255,255),
    5: (0,0,0,0),
    6: (0,0,0,0),
    7: (0,0,0,0),
    8: (0,0,0,0),
    9: (0,0,0,0),
    11: (121,141,205,255),#skin
    12: (34,34,34,255),#shorts
    13: (0,0,255,255),#red
    14: (89,69,4,255),#green
    15: (5,56,182,255),#hair
    16: (89,69,4,255),#shoes
    17: (49,32,46,255),#tshirt
    18: (255,0,0,255),
    19: (0,0,255,255),
}


#Version with random colors
random_255_colors_4_channels = [] 
for i in range(256):
    col = (np.random.randint(0,256), np.random.randint(0,256), np.random.randint(0,256), 255)
    random_255_colors_4_channels.append(col)

'''
color_assignment = { #color from original segmentation (grayscale) to final color
    162: (0,64,158,255)
}
'''


#From aot_tracker.py
np.random.seed(200)
_palette = ((np.random.random((3*255))*0.7+0.3)*255).astype(np.uint8).tolist()
_palette = [0,0,0]+_palette
#c = _palette[id*3:id*3+3] USAGE

#Build our own dictionary for the colors
palette = {}
for i in range(255):
    palette[i] = _palette[i*3:i*3+3]

def idFromColor(palette, c):
    for i in range(255):  
        if palette[i][0] == c[0] and palette[i][1] == c[1] and palette[i][2] == c[2]:
            return i
    return None

def opencv_to_RGB(c):
    return c[::-1]

def simplify(opencvContour, tolerance = 4.0):#5.0 , preserve_topology=False
    """ Simplify a polygon with shapely.
    Polygon: ndarray
        ndarray of the polygon positions of N points with the shape (N,2)
    """
    polygon = np.squeeze(opencvContour)
    poly = shapely.geometry.Polygon(polygon)
    poly_s = poly.simplify(tolerance=tolerance, preserve_topology=False)
    # convert it back to numpy
    coords = np.array(poly_s.boundary.coords[:])
    #Convert shapely polygon (N, 2) to opencv contour (N-1, 1, 2)
    opencvContourSimplified = coords.reshape((-1,1,2)).astype(np.int32)    
    return opencvContourSimplified

def addAlpha(img):
    #b_channel, g_channel, r_channel = cv2.split(img)
    #alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 50 #creating a dummy alpha channel image.
    #img_BGRA = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
    #img_BGRA = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)
    b_channel, g_channel, r_channel = cv2.split(img)
    #alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 0
    alpha_channel = np.zeros(b_channel.shape, dtype=b_channel.dtype)
    img_BGRA = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
    return img_BGRA

def pixelate(input, w, h): # w,h  Desired "pixelated" size
    height, width = input.shape[:2]
    # Resize input to "pixelated" size
    temp = cv2.resize(input, (w, h),  interpolation=cv2.INTER_NEAREST)#cv2.INTER_LINEAR antialiasing
    # Initialize output image
    output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    return output

def getContours(im):
    height, width = im.shape[:2]
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    contours_not_dilated = []
    contours_raw = []
    contours_simplified = []
    colors = []

    #split image in C color regions (with a minimum of 1000 pixels)
    selected_contours = []
    contours_simplified = [] 
    colorNum = 0
    totalContours = 0
    #unique = np.unique(imgray)
    unique_colours = np.unique(im.reshape(-1, im.shape[2]), axis=0)
    #For each COLOR 
    for i, color in enumerate(unique_colours):
        objectId = idFromColor(palette, opencv_to_RGB(color))
        #print("objectId=", objectId)
        mask = cv2.inRange(im, color, color)

        #cv2.imshow("title", mask)
        #cv2.waitKey()

        #im[color_mask==255]=((100+k*50)%255, 100, (objectId*50)%255)

        #mask = np.zeros_like(imgray)
        #mask[imgray == color] = 255
        #mask[imgray == color] = 255
        area = cv2.countNonZero(mask)
        if area > 200 and area < height*width/2: #avoid the frame contour
            
            #cv2.imshow("title", mask)
            #cv2.waitKey()

            #split color mask in N contours (with a minimum of area > 10)
            ret, thresh = cv2.threshold(mask, 127, 255, 0)
            image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            for j, contour in enumerate(contours):
                if cv2.contourArea(contour) > 10:
                    
                    contours_not_dilated.append(contour)
    
                    print("Color (opencv)="+str(colorNum)+"="+str(color))
                    #dilate 1 pixel (to avoid gaps between simplified contours)
                    #remove anything outside the contour
                    part_mask = cropContours(mask, contour)
                    kernel = np.ones((4, 4), np.uint8)
                    part_mask = cv2.dilate(part_mask, kernel, iterations=1)
                    #cv2.imshow("title", part_mask)
                    #cv2.waitKey() 

                    #find contours again
                    ret, thresh = cv2.threshold(part_mask, 127, 255, 0)
                    image, contours_dilated, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
                    max_contour = max(contours_dilated, key = cv2.contourArea)

                    contours_raw.append(max_contour)
                    print("colors.append(opencv_to_RGB("+str(color)+"))")
                    colors.append(opencv_to_RGB(color))
                    test = np.zeros_like(imgray)
                    #cv2.drawContours(test, [max_contour], contourIdx=0, color=(100,200,100), thickness=2)
                    #cv2.imshow("title", test)
                    #cv2.waitKey() 
                    totalContours = totalContours+1                          
            colorNum = colorNum+1
    print("Found "+str(colorNum)+" colors")
    print("Found "+str(totalContours)+" contours")
    return contours_not_dilated, contours_raw, colors

def cropContours(im, contour):
    im_res = np.zeros_like(im)
    cv2.fillPoly(im_res, pts =[contour], color=(255,255,255))
    return im_res

def simplifyContours(contours):
    contours_simplified = []
    for contour in contours:
        try:
            simplifiedContour = simplify(contour)
            contours_simplified.append(simplifiedContour)
        except:
            print("Contour discarded as contains multi-part geometries")
            print(traceback.format_exc())
            print("Using original contour without simplification")
            contours_simplified.append(contour)
    return contours_simplified

#not used
'''
def shadow_contour(contour):
	contour_shifted = np.copy(contour)
	for i in range(len(contour_shifted)):
		contour_shifted[i][0] = contour_shifted[i][0] + 5
	return contour_shifted
#not used
def darkColor(color):
	return (abs(color[0]/2), abs(color[1]/2), abs(color[2]/2), 255)
'''

def fillContours(contours, colors, imcolor):
    for i, contour in enumerate(contours):
        color_id = idFromColor(palette, colors[i])
        print(str(colors[i])+" -> color_id="+str(color_id))
        
        if color_id in color_assignmentNEW:
            display_color = color_assignmentNEW[color_id]
            print("Found assignment for color_id "+str(color_id)+" -> "+str(display_color))
        else:
            print("WARNING: Not found color assignment for color_id ", color_id)
            #display_color = random_255_colors_4_channels[color_id]
            #print("Assignment from list of randoms for color_id "+str(color_id)+" -> "+str(display_color))   
        
        #Assignment from previously randomized list
        #display_color = random_255_colors_4_channels[color_id]
        

        #print("color_id "+str(color_id)+"->"+str(display_color))
        #display_color = np.insert(colors[i], 0, 255)
        #print("display_color=", display_color)
        cv2.fillPoly(imcolor, pts =[contour], color=display_color)

    imcolor_pixelated = pixelate(imcolor, 512, 512)
    #imcolor_pixelated = imcolor
    return imcolor_pixelated

def fillContoursOLD(contours, colors, imcolor):
    for i, contour in enumerate(contours):
        color_id = colors[i]
        if color_id in color_assignment:
            display_color = color_assignment[color_id]
        else:
            display_color = random_255_colors_4_channels[i]
        cv2.fillPoly(imcolor, pts =[contour], color=display_color)
    imcolor_pixelated = pixelate(imcolor, 512, 512)
    return imcolor_pixelated

def change_brightness(img, value=100):
    _, _, _, a_channel = cv2.split(img)
    #img_BGRA = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v,value)
    v[v > 255] = 255
    v[v < 0] = 0
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    img = np.dstack((img, a_channel))
    return img

def addShadow(imcolor, shadowSize=10):    
    imcolor_result_shadow = imcolor.copy()
    height, width = imcolor_result_shadow.shape[:2]
    offsetx = shadowSize
    offsety = 0
    M = np.float32([[1, 0, offsetx], [0, 1, offsety]])
    dst_mat = np.zeros((height, width, 4), np.uint8)
    size = (width, height)
    imcolor_result_shadow = cv2.warpAffine(imcolor_result_shadow, M, size, dst_mat)
    imcolor_result_shadow = change_brightness(imcolor_result_shadow)
    result = overlay(bottomImage=imcolor_result_shadow, topImage=imcolor)
    return result

def overlay(bottomImage, topImage):
	#Idea: add the topImage (complete) to a sliced bottomImage 
    #Obtain an opencvmask from the alpha channel of the topImage
    _, mask = cv2.threshold(topImage[:, :, 3], 0, 255, cv2.THRESH_BINARY)
    #Invert the mask
    mask = cv2.bitwise_not(mask) 
    #Use the mask to cut the intersection from the bottomImage
    bottomImageMinusTopImage = cv2.bitwise_and(bottomImage, bottomImage, mask=mask)
    #Add the topImage (complete) and bottomImageMinusTopImage
    result = bottomImageMinusTopImage + topImage
    return result

def drawContours(contours, colors, imcolor):

    for i, contour in enumerate(contours):
        #color_id = idFromColor(palette, colors[i])
        color_id = idFromColor(palette, colors[i])
        if color_id in color_assignmentNEW:
            display_color = color_assignmentNEW[color_id]
        else:
            display_color = random_255_colors_4_channels[i]
        
        if PRINT_COLOR_IDS:
            # compute the center of the contour
            M = cv2.moments(contour)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.putText(imcolor, str(color_id), (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0,255), 2)
        cv2.drawContours(imcolor, [contour], contourIdx=0, color=display_color, thickness=1)        
    #imcolor_pixelated = pixelate(imcolor, 512, 512)
    return imcolor

if __name__ == "__main__":
    '''
            MAIN
    ''' 
    '''
    np.random.seed(200)
    _palette = ((np.random.random((3*255))*0.7+0.3)*255).astype(np.uint8).tolist()
    _palette = [0,0,0]+_palette
    #c = _palette[id*3:id*3+3] USAGE
    palette = {}
    for i in range(255):
        palette[i] = _palette[i*3:i*3+3]
    im = cv2.imread("060.png")
    im = replaceColors(im, 0, palette)
    cv2.imshow("title", im)
    cv2.waitKey()
    sys.exit(0)
    '''
    
    SCENE_PATH = sys.argv[1]
    if len(sys.argv) > 2:
        addFace = bool(int(sys.argv[2])) #1=yes
        print("Specified addFace=", addFace)
    else:
        addFace = True

    if len(sys.argv) > 3:
        shadowSize = int(sys.argv[3])
        print("Specified shadowSize=", shadowSize)
    else:
        shadowSize = 10
    

    inputpathOriginal = SCENE_PATH+"/imagesFull"
    inputpath = SCENE_PATH+"/samtrack/example_all"
    outputpath = SCENE_PATH+"/out_opencv/"
    outputpath_contours_not_dilated = SCENE_PATH+"/out_opencv_contours_not_dilated/"
    outputpath_contours = SCENE_PATH+"/out_opencv_contours/"
    outputpath_simplify = SCENE_PATH+"/out_opencv_simplify/"
    outputpath_noshadow = SCENE_PATH+"/out_opencv_noshadow/"


    #inputpath = '/Users/rtous/DockerVolume/seg4art/data/scenes/tiktok2/out_pngs'
    #outputpath = '/Users/rtous/DockerVolume/seg4art/data/scenes/tiktok2/out_opencv/'
    #outputpath_contours = '/Users/rtous/DockerVolume/seg4art/data/scenes/tiktok2/out_opencv_contours/'

    if not os.path.exists(outputpath):
       os.makedirs(outputpath)
    if not os.path.exists(outputpath_noshadow):
       os.makedirs(outputpath_contours_not_dilated)
    if not os.path.exists(outputpath_contours_not_dilated):
       os.makedirs(outputpath_contours_not_dilated)
    if not os.path.exists(outputpath_simplify):
       os.makedirs(outputpath_simplify)
    if not os.path.exists(outputpath_noshadow):
       os.makedirs(outputpath_noshadow)

    for filename in sorted(os.listdir(inputpath)):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):# and filename=="00066.png":
            print("process("+inputpath+"/"+filename+", "+outputpath+")")
            #Read image with opencv
            im = cv2.imread(os.path.join(inputpath, filename))
            assert im is not None, "file could not be read, check with os.path.exists()"
           
            #add a border (to avoid edge contours to be discarded)
            #im = cv2.copyMakeBorder(im, 50, 50, 50, 50, cv2.BORDER_CONSTANT, None, value = 0) 

            #cv2.imshow("title", im)
            #cv2.waitKey()
            imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            
            #find relevant contours
            contours_not_dilated, contours_raw, colors = getContours(im)

            #align close contours
            #contours_raw = util_contours.fillGaps(contours_raw)

            #simplify
            contours_simplified = simplifyContours(contours_raw)

            #draw contours, pixelate and write file
            imcolor = np.zeros_like(im)
            imcolor = addAlpha(imcolor)
            imcolor_result = fillContours(contours_simplified, colors, imcolor)
            
            #add shadows
            #write no shadow
            #cv2.imwrite(os.path.join(outputpath_noshadow, filename), imcolor_result)
            imcolor_result = addShadow(imcolor_result, shadowSize)

            #draw face elements
            if addFace:
                facial_landmarks.faceFromPath(os.path.join(inputpathOriginal, filename), imcolor_result)
            
            #write image
            cv2.imwrite(os.path.join(outputpath, filename), imcolor_result)
            print("cv2.imwrite("+os.path.join(outputpath, filename)+")")

            '''
            #contours not dilated
            imcolor_contours = np.zeros_like(im)
            imcolor_contours = addAlpha(imcolor_contours)
            imcolor_contours_result = drawContours(contours_not_dilated, colors, imcolor_contours)    
            cv2.imwrite(os.path.join(outputpath_contours_not_dilated, filename), imcolor_contours_result)
           
            #contours original
            imcolor_contours = np.zeros_like(im)
            imcolor_contours = addAlpha(imcolor_contours)
            imcolor_contours_result = drawContours(contours_raw, colors, imcolor_contours)    
            cv2.imwrite(os.path.join(outputpath_contours, filename), imcolor_contours_result)
            '''

            #contours simplified
            if DRAW_CONTOURS_SIMPLIFIED:
                imcolor_contours = np.zeros_like(im)
                imcolor_contours = addAlpha(imcolor_contours)
                imcolor_contours_result = drawContours(contours_simplified, colors, imcolor_contours)    
                cv2.imwrite(os.path.join(outputpath_simplify, filename), imcolor_contours_result)
                