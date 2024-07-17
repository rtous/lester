import matplotlib.pyplot as plt
import shapely.geometry
import cv2
import numpy as np
import util_contours
import os
from imutils import face_utils
import imutils
import dlib

#From https://datagen.tech/guides/face-recognition/facial-landmarks/

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


def process(inputpath, outputpath):
    print("process("+inputpath+", "+outputpath+")")
    im = cv2.imread(inputpath)
    assert im is not None, "file could not be read, check with os.path.exists()"
    im_res = im #result over the input image
    #im_res = np.zeros_like(im) #empty image for the result
    #im_res = addAlpha(im_res) #add alpha channel (will be saved as png)
    face(im, im_res)
    print("cv2.imwrite("+outputpath+")")
    cv2.imwrite(outputpath, im_res)


def faceFromPath(inputpath, im_res):   
    print("faceFromPath("+inputpath+", im_res)")
    im = cv2.imread(inputpath)
    if im is None:
        path, file_extension = os.path.splitext(inputpath)
        if file_extension==".png":
            print("failed, testing with path: "+path+".jpg")
            im = cv2.imread(path+".jpg")
            print("failed, testing with path: "+path+".png")
        elif file_extension==".jpg":
            im = cv2.imread(path+".png")
    assert im is not None, "file could not be read, check with os.path.exists()"
    face(im, im_res)

#WARNING: landmark number starts from 0, so substract 1 to the number from the reference photo
def face(im, im_res):
    #print("process("+inputpath+", "+outputpath+")")
    #im = cv2.imread(inputpath)
    #im_res = np.zeros_like(im) #empty image for the result
    #im_res = addAlpha(im_res) #add alpha channel (will be saved as png)
    #assert im is not None, "file could not be read, check with os.path.exists()"
    #height, width = im.shape[:2]
    # initialize built-in face detector in dlib
    detector = dlib.get_frontal_face_detector()
    # initialize face landmark predictor
    PREDICTOR_PATH = "./models/shape_predictor_68_face_landmarks.dat"#https://github.com/davisking/dlib-models
    predictor = dlib.shape_predictor(PREDICTOR_PATH)
    #resize to width 500
    #im_resized = cv2.resize(im, (500, 500), interpolation= cv2.INTER_LINEAR)
    #Resizing accelerates but you need to upscale everything later
    image = im
    #image = imutils.resize(im, width=500)
    #convert it to grayscale
    im_resized_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # detect faces in the grayscale image
    rects = detector(im_resized_gray, 1)
    #for each face
    for (i, rect) in enumerate(rects):
        # predict facial landmarks in image and convert to NumPy array
        shape = predictor(im_resized_gray, rect)

        draw_eyes_contour(shape, im_res)

        draw_pupils(shape, im_res) 

        draw_nose(shape, im_res)

        draw_mouth(shape, im_res)


        shape = face_utils.shape_to_np(shape)

        left_eye = shape[37:42]
        right_eye = shape[43:48]
        nose_base = shape[32:36]
        mouth_exterior = shape[49:60]
        mouth_interior = shape[61:68]
        
            
        #cv2.drawContours(im_res, [mouth_exterior], 0, (0,255,0,255), 1)
        #cv2.drawContours(im_res, [left_eye], 0, (0,255,0,255), 1)
        #cv2.drawContours(im_res, [right_eye], 0, (0,255,0,255), 1)
        #jawline = shape[0:17]

        # convert to OpenCV-style bounding box
        #for (x, y) in shape:
        x, y, w, h = rect.left(), rect.top(), rect.width(), rect.height()

        #draw all landmarks
        #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #for (i, (x, y)) in enumerate(shape):
        #    cv2.putText(image, str(i + 1), (x - 10, y - 10),
        #        cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
        #    cv2.circle(image, (x, y), 1, (0, 0, 255), -1)

        # show the resulting output image
        #cv2.imshow("Output", image)
        #cv2.waitKey(0)

def draw_nose(shape, im_res):
    eye_contour = np.array([
            [shape.part(31).x, shape.part(31).y], [shape.part(33).x, shape.part(33).y], 
            [shape.part(33).x, shape.part(33).y], [shape.part(35).x, shape.part(35).y], 
            [shape.part(35).x, shape.part(35).y], [shape.part(31).x, shape.part(31).y]
            ], np.int32)
    
    pts = eye_contour.reshape((-1, 1, 2))
    #im_res = cv2.polylines(im_res, [pts], True, (199, 199, 199, 255), 1)
    cv2.fillPoly(im_res, [pts], color = (118, 113, 168, 255))

def draw_mouth(shape, im_res):
    #The numbers in the image start in 1, so need to reduce them by 1

    '''
    thickness = 
    eye_contour = np.array([
            [shape.part(48).x, shape.part(48).y], [shape.part(54).x, shape.part(54).y]
            ], np.int32)
    
    pts = eye_contour.reshape((-1, 1, 2))
    im_res = cv2.polylines(im_res, [pts], True, (199, 199, 199, 255), 1)
    '''



    
    x_plus_top = int(shape.part(49).x - shape.part(53).x)/3
    x_plus_bottom = int(shape.part(55).x - shape.part(59).x)/3
    y_plus_left = int(shape.part(49).y - shape.part(59).y)/3
    y_plus_right = int(shape.part(53).y - shape.part(55).y)/3
    '''eye_contour = np.array([
            [shape.part(49).x + x_plus_top, shape.part(49).y - y_plus_left], [shape.part(53).x - x_plus_top, shape.part(53).y - y_plus_right], 
            [shape.part(53).x - x_plus_top, shape.part(53).y - y_plus_right], [shape.part(55).x + x_plus_bottom, shape.part(55).y + y_plus_right], 
            [shape.part(55).x + x_plus_bottom, shape.part(55).y + y_plus_right], [shape.part(59).x - x_plus_bottom, shape.part(59).y + y_plus_right],
            [shape.part(59).x - x_plus_bottom, shape.part(59).y + y_plus_left], [shape.part(49).x + x_plus_top, shape.part(49).y - y_plus_left]
            ], np.int32)'''

    shape = face_utils.shape_to_np(shape)
    
    '''
    lips_contour = shape[48:59] #mouth interior
    pts = lips_contour.reshape((-1, 1, 2))
    #im_res = cv2.polylines(im_res, [pts], True, (199, 199, 199, 255), 1)
    cv2.fillPoly(im_res, [pts], color = (118, 113, 168, 255))
    '''

    mouth_contour = shape[60:67] #mouth interior
    pts = mouth_contour.reshape((-1, 1, 2))
    #im_res = cv2.polylines(im_res, [pts], True, (199, 199, 199, 255), 1)
    cv2.fillPoly(im_res, [pts], color = (118, 113, 168, 255))

def draw_mouthOLD(shape, im_res):
    '''
    thickness = 
    eye_contour = np.array([
            [shape.part(48).x, shape.part(48).y], [shape.part(54).x, shape.part(54).y]
            ], np.int32)
    
    pts = eye_contour.reshape((-1, 1, 2))
    im_res = cv2.polylines(im_res, [pts], True, (199, 199, 199, 255), 1)
    '''

    
    x_plus_top = int(shape.part(49).x - shape.part(53).x)/3
    x_plus_bottom = int(shape.part(55).x - shape.part(59).x)/3
    y_plus_left = int(shape.part(49).y - shape.part(59).y)/3
    y_plus_right = int(shape.part(53).y - shape.part(55).y)/3
    eye_contour = np.array([
            [shape.part(49).x + x_plus_top, shape.part(49).y - y_plus_left], [shape.part(53).x - x_plus_top, shape.part(53).y - y_plus_right], 
            [shape.part(53).x - x_plus_top, shape.part(53).y - y_plus_right], [shape.part(55).x + x_plus_bottom, shape.part(55).y + y_plus_right], 
            [shape.part(55).x + x_plus_bottom, shape.part(55).y + y_plus_right], [shape.part(59).x - x_plus_bottom, shape.part(59).y + y_plus_right],
            [shape.part(59).x - x_plus_bottom, shape.part(59).y + y_plus_left], [shape.part(49).x + x_plus_top, shape.part(49).y - y_plus_left]
            ], np.int32)
    
    pts = eye_contour.reshape((-1, 1, 2))
    #im_res = cv2.polylines(im_res, [pts], True, (199, 199, 199, 255), 1)
    cv2.fillPoly(im_res, [pts], color = (118, 113, 168, 255))
    

def draw_eyes_contour(shape, im_res):
    x_plus_top = int(shape.part(37).x - shape.part(44).x)/4
    x_plus_bottom = int(shape.part(46).x - shape.part(41).x)/4
    y_plus_left = int(shape.part(37).y - shape.part(41).y)/5
    y_plus_right = int(shape.part(44).y - shape.part(46).y)/5
    eye_contour = np.array([
            [shape.part(37).x + x_plus_top, shape.part(37).y + y_plus_left], [shape.part(44).x - x_plus_top, shape.part(44).y + y_plus_right], 
            [shape.part(44).x - x_plus_top, shape.part(44).y + y_plus_right], [shape.part(46).x + x_plus_bottom, shape.part(46).y - y_plus_right], 
            [shape.part(46).x + x_plus_bottom, shape.part(46).y - y_plus_right], [shape.part(41).x - x_plus_bottom, shape.part(41).y - y_plus_right],
            [shape.part(41).x - x_plus_bottom, shape.part(41).y - y_plus_left], [shape.part(37).x + x_plus_top, shape.part(37).y + y_plus_left]
            ], np.int32)
    
    pts = eye_contour.reshape((-1, 1, 2))
    #im_res = cv2.polylines(im_res, [pts], True, (199, 199, 199, 255), 1)
    cv2.fillPoly(im_res, [pts], color = (118, 113, 168, 255))

def draw_pupils(shape, im_res, color=(61, 71, 118, 255)):

    radius = int(abs(shape.part(39).x - shape.part(36).x)/4)
    pupil_x = int((abs(shape.part(39).x + shape.part(36).x)) / 2)
    pupil_y = int((abs(shape.part(39).y + shape.part(36).y)) / 2)
    pupil = (pupil_x, pupil_y)
    cv2.circle(im_res, pupil, radius, color, thickness=-1) #-1 means fill

    radius = int(abs(shape.part(42).x - shape.part(45).x)/4)
    pupil_x = int((abs(shape.part(42).x + shape.part(45).x)) / 2)
    pupil_y = int((abs(shape.part(42).y + shape.part(45).y)) / 2)
    pupil = (pupil_x, pupil_y)
    cv2.circle(im_res, pupil, radius, color, thickness=-1) #-1 means fill
    


if __name__ == "__main__":
    inputpath = '/Users/rtous/DockerVolume/seg4art/data/scenes/ruben2/imagesFull'
    outputpath = '/Users/rtous/DockerVolume/seg4art/data/scenes/ruben2/out_face/'
    if not os.path.exists(outputpath):
        os.makedirs(outputpath)
    for filename in sorted(os.listdir(inputpath)):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            process(os.path.join(inputpath, filename), os.path.join(outputpath, filename))

