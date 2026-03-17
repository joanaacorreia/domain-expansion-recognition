import cv2
import mediapipe as mp


class HandTracker:
    def __init__(self):
        self.detector = mp.solutions.hands.Hands()
        self.drawingTool = mp.solutions.drawing_utils
        
    def findHands(self, frame):
        rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.detector.process(rgbFrame)
        
        if result.multi_hand_landmarks:
            for handLandmarks in result.multi_hand_landmarks:
                self.drawingTool.draw_landmarks(
                    frame, 
                    handLandmarks, 
                    mp.solutions.hands.HAND_CONNECTIONS
                )
                
        return frame