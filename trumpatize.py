import cv2

# Face recognition stuff
cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)


# Hat constants
REDHAT = 1
WHITEHAT = 2
CAMOHAT = 3
HAIR = 4

# Hat image for placement on heads
red_maga_hat_img = cv2.imread("img/MAGA_hat_x200.png", -1)
white_maga_hat_img = cv2.imread("img/MAGA_white.png", -1)
camo_maga_hat_img = cv2.imread("img/MAGA_camo.png", -1)
hair_img = cv2.imread("img/trump_hair.png", -1)


def addhat(frame):
    """:returns an image with the default hat type (red)"""
    return addhat_red(frame)


def addhat_red(frame):
    return __addhat(frame, REDHAT)


def __addhat(frame, hat_type):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    try:
        if faces.any():
            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:

                # Switch hat type
                if hat_type == REDHAT:
                    hat_img = red_maga_hat_img
                elif hat_type == WHITEHAT:
                    hat_img = white_maga_hat_img
                elif hat_type == CAMOHAT:
                    hat_type == camo_maga_hat_img
                elif hat_type == HAIR:
                    hat_type == hair_img
                else:
                    hat_img = red_maga_hat_img

                # Draw MAGA hat
                hat_height = hat_img.shape[0]
                hat_width = hat_img.shape[1]
                # Image scale based on face width
                scale = w*1.0/hat_width
                hat_height = int(hat_height*scale)
                hat_img = cv2.resize(hat_img, (w, hat_height), interpolation=cv2.INTER_AREA)
                x_offset = x
                y_offset = max(0, y - hat_height)
                for c in range(0,3):
                    # http://stackoverflow.com/questions/14063070/overlay-a-smaller-image-on-a-larger-image-python-opencv/14102014#14102014
                    frame[y_offset:y_offset + hat_img.shape[0], x_offset:x_offset + hat_img.shape[1], c] = \
                        hat_img[:, :, c] * (hat_img[:, :, 3] / 255.0) + frame[y_offset:y_offset + hat_img.shape[0], x_offset:x_offset + hat_img.shape[1], c] * (1.0 - hat_img[:, :, 3] / 255.0)
            #print 'Faces'
        #else:
            #print 'No faces?'
    # Catch an Attribute error.  This will be thrown if attempting to invoke .any() on
    # an empty list of faces (specific error:  'tuple' object has no attribute 'any')
    except AttributeError:
        #print 'No faces here'
        pass

    return frame

