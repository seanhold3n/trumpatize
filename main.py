# Derived from
# https://github.com/shantnu/Webcam-Face-Detect, via
# https://realpython.com/blog/python/face-detection-in-python-using-a-webcam/
import cv2
import trumpatize

video_capture = cv2.VideoCapture(0)


while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    frame = trumpatize.addhat(frame)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
