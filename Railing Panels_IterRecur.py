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
#middle point on selected curve
domain = rs.CurveDomain(crvIterative)
t = domain[1]/2.0
point = rs.EvaluateCurve(crvIterative, t)
startPoint = rs.AddPoint(point)

def recursivePanel(startPoint, lengthPanel):
"""it works only with this rules:
circle just cut crv in two points, this means crv is more
or less strait and do not have flowers on int"""
    
    #building the core
    circleAux = rs.AddCircle(startPoint, lengthPanel)
    pEnd = rs.CurveCurveIntersection(crvIterative, circleAux)
    
    if len(pEnd) == 2:
        #first middle curve
        panelA = rs.AddLine(startPoint, pEnd[0][1])
        recursivePanel(pEnd[0][1], lengthPanel)
        
        #second middle curve
        #not working... perhaps it worth make a copy of elements to be reused
        #panelB = rs.AddLine(startPoint, pEnd2[1][1])
        #recursivePanel(pEnd[1][1], lengthPanel)
    
    
#iterativePanel(2)
recursivePanel(startPoint, 3)