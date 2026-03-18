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
        
        
    def isFingerUp(self, landmarks, fingerTipId, knuckleId):
        return landmarks[fingerTipId][1] < landmarks[knuckleId][1]
    
    
    def isThumbUp(self, landmarks, fingerTipId, knuckleId):
        return landmarks[fingerTipId][0] > landmarks[knuckleId][0]
    
    
    def detectMalevolentShrine(self, hands): 
        # get the first hand
        hand = hands[0]
        
        # index and pinky fingers down
        indexDown = not self.isFingerUp(hand, 8, 6) 
        pinkyDown = not self.isFingerUp(hand, 20, 18)
        
        # middle and ring fingers up
        middleUp = self.isFingerUp(hand, 12, 10)
        ringUp = self.isFingerUp(hand, 16, 14)
        
        # thumb up 
        thumbUp = self.isThumbUp(hand, 4, 2)
        
        return all([
            indexDown, 
            pinkyDown, 
            middleUp, 
            ringUp, 
            thumbUp
        ])
    
    
    def detectUnlimitedVoid(self, hands):
        pass
    
    
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
    
