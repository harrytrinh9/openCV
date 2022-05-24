import cv2 as cv
import os

cascPath=os.path.dirname(cv.__file__)+"/data/haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(cascPath)
video_capture = cv.VideoCapture(0)
video_capture.set(3, 640) # set width 1280
video_capture.set(4, 480) # set heigh 960

while True:
    # Capture frame-by-frame
    ret, frames = video_capture.read()
    gray = cv.cvtColor(frames, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv.CASCADE_SCALE_IMAGE
    )
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Display the resulting frame
    cv.imshow('Video', frames)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv.destroyAllWindows()