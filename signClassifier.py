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
        # sign is symmetrical, only need one hand
        hand = hands[0]
        
        # index and pinky down
        indexDown = not self.isFingerUp(hand, 8, 6) 
        pinkyDown = not self.isFingerUp(hand, 20, 18)
        
        # middle, ring, and thumb up
        middleUp = self.isFingerUp(hand, 12, 10)
        ringUp = self.isFingerUp(hand, 16, 14)
        thumbUp = self.isThumbUp(hand, 4, 2)
        
        return all([
            indexDown, 
            pinkyDown, 
            middleUp, 
            ringUp, 
            thumbUp
        ])
    
    
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
        
        return all([
            indexUp, 
            thumbUp, 
            ringDown, 
            pinkyDown,
            middleBent
        ])

    
    def detectChimeraShadowGarden(self, hands):
        pass
    
    
    def detectSelfEmbodimentPerfection(self, hands):
        pass
    
    
    def detectWombProfusion(self, hands):
        pass
    
    
    def detectIdleDeathGamble(self, hands):
        pass
    
    
    def detectTimeCellMoonPalace(self, hands):
        pass
    
