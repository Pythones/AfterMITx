#PanelonRail_Recursive
#140424 Pythones@Manu

import rhinoscriptsyntax as rs

def iterativePanel(lengthPanel):
    
    #aux elements
    crvBase = rs.GetObject("Iterative mode, Select curve to be use as rail", rs.filter.curve)
    #domain for split the curve into equal parts
    domain = rs.CurveDomain(crvBase)
    t = domain[1]/2.0
    crvSplit = rs.SplitCurve(crvBase, t)
    
    #building the core
    pEnd = rs.DivideCurveEquidistant(crvSplit[1], lengthPanel, True)
        
    for i in range (len(pEnd)-1):
        #rs.AddCircle(pEnd[i], 5) #Just fot testing
        panel = rs.AddLine(pEnd[i], pEnd[i+1])
        
        
#elements needed prior run function
crvIterative = rs.GetObject("Recursive Mode, Select curve to be use as rail", rs.filter.curve)

domain = rs.CurveDomain(crvIterative)
t = domain[1]/2.0
point = rs.EvaluateCurve(crvIterative, t)
startPoint = rs.AddPoint(point)

#startPoint = rs.CurveStartPoint(crvIterative)

def recursivePanel(startPoint, lengthPanel):
    
    #building the core
    circleAux = rs.AddCircle(startPoint, lengthPanel)
    pEnd = rs.CurveCurveIntersection(crvIterative, circleAux)
    
    if pEnd:
	#second middle curve
        panelA = rs.AddLine(startPoint, pEnd[1][1])
        recursivePanel(pEnd[1][1], lengthPanel)
	
	#first middle curve, not working
	#panelB = rs.AddLine(startPoint, pEnd[0][2])
        #recursivePanel(pEnd[0][2], lengthPanel)
        
        
#iterativePanel(3)
recursivePanel(startPoint, 3)