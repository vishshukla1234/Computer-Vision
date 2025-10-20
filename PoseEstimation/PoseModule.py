import cv2 as cv
import mediapipe as mp
import time


class poseDetector():
    def __init__(self, mode=False, upBody=False,smooth=True,detectionCon=0.5,trackCon=0.5):

        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(
                static_image_mode=self.mode,
                model_complexity=1,
                smooth_landmarks=self.smooth,
                enable_segmentation=False,
                min_detection_confidence=self.detectionCon,
                min_tracking_confidence=self.trackCon
            )


    def findPose(self, img,draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
                
        return img
    
    def findPosition(self,img,draw=True):
        lmList = []
        if self.results.pose_landmarks:
            for(id, lm) in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id,cx,cy])
                if draw:
                    cv.circle(img,(cx,cy),10,(255,0,255),cv.FILLED)

        return lmList


def main():
    cap = cv.VideoCapture('PoseEstimation/3.mp4')

    pTime = 0
    detector = poseDetector()
    while True:
        success, img = cap.read()
        if not success:
            break

        img = detector.findPose(img)
        lmList = detector.findPose(img)
        print(lmList[14])

        cTime = time.time()
        fps = 1 / (cTime - pTime) if (cTime - pTime) != 0 else 0
        pTime = cTime
        
        cv.putText(img, str(int(fps)), (70,50), cv.FONT_HERSHEY_PLAIN, 3, (255,0,0),3)
        cv.imshow("Image",img)
        # Press 'q' to quit
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()



if __name__ == "__main__":
    main()