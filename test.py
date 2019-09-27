from streamz import Stream
import cv2
import time


# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

save_location = "/Users/jdyer/Desktop/rtsp_images"

def save_frame(frame):
    filename = save_location + "/" + str(time.time()) + '.jpg'
    resp = cv2.imwrite(filename, frame)
    return "RTSP Frame saved to: {}".format(filename)

def parse_frame(frame):
    cv2.imshow('frame', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print("gray")
    print(gray)
    return frame


source = Stream.from_rtsp("192.168.1.200", username="admin", password="Rascal18")
output = source.map(save_frame)
source.start()

while True:
    time.sleep(2)