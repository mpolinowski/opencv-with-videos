import cv2

cap = cv2.VideoCapture("recording/captured_video.mp4")

while (True):
    ret, frame = cap.read()
    cv2.imshow("Video Recording", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print('Video was saved!')