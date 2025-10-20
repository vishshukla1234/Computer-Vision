import cv2 as cv
import numpy as np
import time
import HandTracking as ht
import autopy

wCam, hCam = 640,480
wScr,hScr = autopy.screen.size()
# print(wScr,hScr)

cap = cv.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
detector = ht.handDetector(maxHands=1)

pTime = 0
frameR = 100 #Frame Reduction
smoothening = 10
plocX,plocY = 0,0
clocX,cloxY = 0,0

while True:
    # 1. Find hand LandMarks
    success, img = cap.read()
    if not success:
        break
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # 2. Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1,y1 = lmList[8][1:]
        x2,y2 = lmList[12][1:]

        # print(x1,y1,x2,y2)

    # 3. Check which fingers are up
    fingers = detector.fingersUp()
    # print(fingers)
    # 4. Only index finger: Moving Mode
    cv.rectangle(img, (frameR,frameR), (wCam-frameR, hCam-frameR),(255,0,0),2)
    if len(fingers) >= 3:
        if fingers[1] == 1 and fingers[2] == 0:
            # 5. Convert Coordinates
            x3 = np.interp(x1,(frameR,wCam-frameR),(0,wScr))
            y3 = np.interp(y1,(frameR,hCam-frameR),(0,hScr))
            # 6. Smoothen Values
            clocX = plocX+(x3-plocX)/smoothening
            clocY = plocY+(y3-plocY)/smoothening
            # 7. Move mouse
            autopy.mouse.move(wScr-clocX,clocY)
            cv.circle(img,(x1,y1), 15, (255,0,0),cv.FILLED)
            plocX,plocY = clocX,clocY
    # 8. Both index and middle fingers are up -> clicking mode
    if len(fingers) >= 3:
        if fingers[1] == 1 and fingers[2] == 1:
            # 9. Find distances btwn fingers
            length, img, lineInfo = detector.findDistance(8,12,img)
            print(length)
            if length <= 30:
                cv.circle(img,(lineInfo[4],lineInfo[5]),
                           15, (0,255,0),cv.FILLED)
                # 10. Click mouse if dist. short
                autopy.mouse.click()

    # 11. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime) if (cTime - pTime) != 0 else 0
    pTime = cTime
    cv.putText(img, str(int(fps)), (10,50), cv.FONT_HERSHEY_PLAIN, 3,(255,0,0),3)
    # 12. Display
    cv.imshow("Img", img)
    cv.waitKey(1)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

