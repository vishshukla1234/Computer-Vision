import cv2 as cv
import mediapipe as mp
import time
import HandTracking as ht


pTime = 0
cTime = 0
# Initialize webcam
cap = cv.VideoCapture(0)
detector = ht.handDetector()
while True:
    success, img = cap.read()
    if not success:
        break
    img=detector.findHands(img)
    lmList = detector.findPosition(img) 
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv.putText(img, f'FPS: {int(fps)}', (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv.imshow("Hand Tracking", img)

        # Press 'q' to quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()