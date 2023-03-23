import numpy as np

class Fuzzy(object):
    def __init__(self):
        self.MF_Value = 0
        pass

    def MembershipFun(self, dist):
        if dist <= -2:
            self.MF_Value = self.MF_RightTurn(dist)
        elif dist <= -1 and dist > -2:
            self.MF_Value = min(self.MF_RightTurn(dist=dist), self.MF_LeftTurn(dist=dist))
        elif dist <= 1 and dist > -1:
            self.MF_Value = self.MF_Straight(dist=dist)
        elif dist <= 2 and dist > 1:
            self.MF_Value = min(self.MF_Straight(dist=dist), self.MF_LeftTurn(dist=dist))
        elif dist > 2:
            self.MF_Value = self.MF_LeftTurn(dist=dist)
        return self.MF_Value
    
    def MF_RightTurn(self, dist):
        MF_Value = 0
        if dist < -4:
            MF_Value = 1
        elif dist < -1 and dist >= -4:
            MF_Value = (-1 - dist) / (-1 - (-4)) 
        else:
            MF_Value = 0
        return float(MF_Value)

    def MF_Straight(self, dist):
        MF_Value = 0
        if dist <= 0:
            MF_Value = (dist - (-2)) / 0 - (-2)
        elif dist > 1:
            MF_Value = (2 - dist) / (2 - 0) 
        else:
            MF_Value = 0
        return float(MF_Value)

    def MF_LeftTurn(self, dist):
        MF_Value = 0
        if dist >= 4:
            MF_Value = 1
        elif dist < 4 and dist >= 1:
            MF_Value = (dist - 1) / (4 - 1) 
        else:
            MF_Value = 0
        return float(MF_Value)
    
if __name__ == "__main__":
    MyFuzzy = Fuzzy()
    print(MyFuzzy.MembershipFun(3))
