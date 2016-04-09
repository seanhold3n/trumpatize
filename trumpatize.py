import cv2

# Face recognition stuff
cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)


# Hat image for placement on heads
red_maga_hat_img = cv2.imread("img/MAGA_hat_x200.png", -1)
rmhi_width = 200  # TODO there is probably a way to get these values from the image
rmhi_height = 144

def addhat(frame):

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
                #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                # Draw MAGA hat
                hat_img = red_maga_hat_img
                # Image scale based on face width
                scale = w*1.0/rmhi_width #TODO get this from hat_img
                hat_height = int(rmhi_height*scale)
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

