#PanelonRail_Classe
#140424 Pythones@Manu

import rhinoscriptsyntax as rs

#starting whith the base class
class PanelonRailBase(object):
    
    #building the constructor
    def __init__(self, Crv, pStart, pEnd, basePanel):
        self.Crv = Crv
        self.pStart = pStart
        self.pEnd = pEnd
        self.basePanel = basePanel
        
    def setCurve(self):
        self.Crv = rs.GetObject("Select the curve to be use as rail", rs.filter.curve)
        return self.Crv
    #doubt: we need pSatar to be iterative, better not to set always at the same place
    #perhaps this def is not necessary
    def setpStart(self):
        self.pStart = rs.EvaluateCurve(self.Crv, 0)
        return self.pStart
        
    def getpEnd(self):
        circle = rs.AddCircle(self.pStart, 1)
        self.pEnd = rs.CurveCurveIntersection(self.Crv, circle)
        return self.pEnd
        

#starting whith the new class
class buildingPanels(PanelonRailBase):
    
    #building the constructor
    def __init__(self, line):
        self.line = line
        
    #NewsStory also needs to contain the following methods
    def getLine(self):
        self.line = rs.AddLine(self.pStart, self.pEnd)
        return self.line