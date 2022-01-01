# the following is an example from "https://stackoverflow.com/questions/2601194/displaying-a-webcam-feed-using-opencv-and-python/11449901#11449901"

import cv2

cv2.namedWindow("preview")
video_capture = cv2.VideoCapture(0)

if video_capture.isOpened(): # try to get the first frame
    rval, frame = video_capture.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = video_capture.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

video_capture.release()
cv2.destroyWindow("preview")
