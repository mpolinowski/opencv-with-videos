import cv2
import os

RTSP_URL = 'rtsp://admin:instar@192.168.2.19/livestream/13'

os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp' # Use tcp instead of udp if stream is unstable

cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print('Cannot open RTSP stream')
    exit(-1)

while True:
    success, img = cap.read()
    cv2.imshow('RTSP stream', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Keep running until you press `q`
        cap.release()
        break

cv2.destroyAllWindows()