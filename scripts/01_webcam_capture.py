import cv2

webcam = cv2.VideoCapture(0)

while (True):
    ret_, frame = webcam.read()
    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        webcam.release()
        break

cv2.destroyAllWindows()