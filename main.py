import cv2
import time

from handTracker import HandTracker

webcam = cv2.VideoCapture(0)
tracker = HandTracker()
time.sleep(2)

lastFrameTime = 0

while True:
    frameSuccess, frame = webcam.read()
    
    if not frameSuccess:
        continue
    
    # calculate fps
    thisFrameTime = time.time()
    timeDiff = thisFrameTime - lastFrameTime
    
    if timeDiff > 0:
        fps = 1 / timeDiff
        
    lastFrameTime = thisFrameTime
    
    # draw FPS on the frame
    cv2.putText(
        frame, 
        f"FPS: {int(fps)}", 
        (10, 30), 
        cv2.FONT_HERSHEY_PLAIN, 
        1, 
        (255,105,180), 
        2
    )

    frame = tracker.findHands(frame)
    cv2.imshow("Domain Expansion", frame)
    cv2.waitKey(1)

    # prop_visible has to be 0 for window to close
    if cv2.getWindowProperty("Domain Expansion", cv2.WND_PROP_VISIBLE) < 1:
        break

webcam.release()
cv2.destroyAllWindows()