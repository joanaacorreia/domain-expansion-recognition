# hand landmark anatomy reference:
# fingertips = tipId
# distal interphalangeal joints = dipId
# proximal interphalangeal joints = pipId
# metacarpophalangeal joints = mcpId

class SignClassifier:
    def __init__(self):
        self.signs = {
            "Malevolent Shrine" : self.detectMalevolentShrine,
            "Unlimited Void" : self.detectUnlimitedVoid,
            "Chimera Shadow Garden" : self.detectChimeraShadowGarden,
            "Self-Embodiment of Perfection" : self.detectSelfEmbodimentPerfection,
            "Womb Profusion" : self.detectWombProfusion,
            "Idle Death Gamble" : self.detectIdleDeathGamble,
            "Time Cell Moon Palace" : self.detectTimeCellMoonPalace,
        }
      
        
    def classify(self, hands):
        if not hands:
            return None
        
        for sign, detectionFunction in self.signs.items():
            if detectionFunction(hands):
                return sign
            
        return None
    
        
    def isFingerUp(self, landmarks, tipId, pipId):
        tipY = landmarks[tipId][1]
        pipY = landmarks[pipId][1]
        
        return tipY < pipY
    
    
    def isThumbUp(self, landmarks, tipId, pipId):
        tipX = landmarks[tipId][0]
        pipX = landmarks[pipId][0]
        
        return tipX > pipX
    
    
    def isFingerBent(self, landmarks, tipId, dipId, mcpId):
        tipY = landmarks[tipId][1]
        dipY = landmarks[dipId][1]
        mcpY = landmarks[mcpId][1]
        
        return tipY > dipY and tipY < mcpY
    
    
    def detectMalevolentShrine(self, hands): 
        if len(hands) < 2:
            return False
    
        hand1 = hands[0]
        hand2 = hands[1]
        
        # hand1 : index and pinky down
        index1Down = not self.isFingerUp(hand1, 8, 6) 
        pinky1Down = not self.isFingerUp(hand1, 20, 18)
        
        # hand1 : middle, ring, and thumb up
        middle1Up = self.isFingerUp(hand1, 12, 10)
        ring1Up = self.isFingerUp(hand1, 16, 14)
        thumb1Up = self.isThumbUp(hand1, 4, 2)
        
        # hand2 : index and pinky down
        index2Down = not self.isFingerUp(hand2, 8, 6)
        pinky2Down = not self.isFingerUp(hand2, 20, 18)
        
        # hand2 : middle, ring, and thumb up
        middle2Up = self.isFingerUp(hand2, 12, 10)
        ring2Up = self.isFingerUp(hand2, 16, 14)
        thumb2Up = self.isThumbUp(hand2, 4, 2)
        
        hand1Match = all([index1Down, pinky1Down, middle1Up, ring1Up, thumb1Up])
        hand2Match = all([index2Down, pinky2Down, middle2Up, ring2Up, thumb2Up])
        
        return hand1Match and hand2Match
    
    
    def detectUnlimitedVoid(self, hands):
        # gojo's sign uses one hand only
        hand = hands[0]
        
        # index and thumb up
        indexUp = self.isFingerUp(hand, 8, 6)
        thumbUp = self.isThumbUp(hand, 4, 2)
        
        # ring and pinky down
        ringDown = not self.isFingerUp(hand, 16, 14)
        pinkyDown = not self.isFingerUp(hand, 20, 18)
        
        # middle bent
        middleBent = self.isFingerBent(hand, 12, 11, 9)
        
        handMatch = all([indexUp, thumbUp, ringDown, pinkyDown, middleBent])
        
        return handMatch

    
    def detectChimeraShadowGarden(self, hands):
        if len(hands) < 2:
            return False
        
        hand1 = hands[0]
        hand2 = hands[1]
        
        # check if hands are closed together
        wrist1X = hand1[0][0]  
        wrist2X = hand2[0][0]
        handsClose = abs(wrist1X - wrist2X) < 0.2
        
        # hand1 : all fingers down, thumb up
        index1Down = not self.isFingerUp(hand1, 8, 6)
        middle1Down = not self.isFingerUp(hand1, 12, 10)
        ring1Down = not self.isFingerUp(hand1, 16, 14)
        pinky1Down = not self.isFingerUp(hand1, 20, 18)
        thumb1Up = self.isThumbUp(hand1, 4, 2)
        
        # hand2 : all fingers down, thumb up
        index2Down = not self.isFingerUp(hand2, 8, 6)
        middle2Down = not self.isFingerUp(hand2, 12, 10)
        ring2Down = not self.isFingerUp(hand2, 16, 14)
        pinky2Down = not self.isFingerUp(hand2, 20, 18)
        thumb2Up = self.isThumbUp(hand2, 4, 2)
        
        hand1Match = all([index1Down, middle1Down, ring1Down, pinky1Down, thumb1Up])
        hand2Match = all([index2Down, middle2Down, ring2Down, pinky2Down, thumb2Up])
        
        return handsClose and hand1Match and hand2Match
    
    
    def detectSelfEmbodimentPerfection(self, hands):
        pass
    
    
    def detectWombProfusion(self, hands):
        pass
    
    
    def detectIdleDeathGamble(self, hands):
        pass
    
    
    def detectTimeCellMoonPalace(self, hands):
        pass
    
