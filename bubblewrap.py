# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 13:17:21 2017

@author: The Users
"""

widthOfLayer = 0.005


import numpy as np
import matplotlib.pyplot as plt

#setting constants
humanMass = 60
humanHeight = 0.65*2.54
humanDensity = 1000
gravity = 9.81
airDensity = 1.025
dragCoefficient = 0.5
dropHeight = 5000

aAxis = 0.11
bAxis = 0.26

bubblewrapDensity = 4
bubblewrapThickness = 0.05#0.001*(25.4*(5/16))


projectionArea = humanHeight * bAxis * 2
print('projection area is', projectionArea)

#initialising variables
totalEllipsePerimeter = 0
ellipsePerimeter = 2 * np.pi * ((aAxis**2 + bAxis**2)/2)**0.5
totalEllipsePerimeter = 0

print('ellipse perimeter is', ellipsePerimeter)
surfaceArea = ellipsePerimeter * humanHeight
print ('surface area is', surfaceArea)

totalBubblewrapArea = 0
totalBubblewrapVolume = 0
bubblewrapMass = 0
totalMass = humanMass + bubblewrapMass

terminalVelocity = ((2*totalMass*gravity)/
                    (dragCoefficient*airDensity*projectionArea))**0.5                    
print('terminal Velocity is', terminalVelocity)

for layer in range(1, 16):#testing results of every layer
    print('layer', layer)
    
    print('aAxis is', aAxis)
    print('bAxis is', bAxis)
    
    ellipsePerimeter = 2 * np.pi * ((aAxis**2 + bAxis**2)/2)**0.5
    print('perimeter is', ellipsePerimeter)
    
    surfaceArea = ellipsePerimeter * humanHeight    
    print('surface area is', surfaceArea)
    
    totalBubblewrapArea = totalBubblewrapArea + surfaceArea
    print('total bubble wrap area is', totalBubblewrapArea)
    
    totalBubblewrapVolume = totalBubblewrapArea * bubblewrapThickness
    print('total bubble wrap volume is', totalBubblewrapVolume)
    
    bubblewrapMass = totalBubblewrapVolume * bubblewrapDensity
    print('total bubble wrap mass is', bubblewrapMass)
    
    totalMass = totalMass + bubblewrapMass
    print('total mass is', totalMass)
    
    projectionArea = humanHeight * bAxis * 2
    print('projection area is', projectionArea)
    
    terminalVelocity = ((2*totalMass*gravity)/
                        (dragCoefficient*airDensity*projectionArea))**0.5                    
    print('terminal Velocity is', terminalVelocity)
    
    impactDistance = layer * bubblewrapThickness
    print('impact distance is', impactDistance)
    
    deceleration = (terminalVelocity**2)/(impactDistance+(aAxis*1))
    stoppingGs = deceleration/gravity
    print('deceleration is', deceleration)
    print('deceleration is', stoppingGs, 'Gs')
    
    stoppingTime = impactDistance/terminalVelocity
    print('stopping time is', stoppingTime)    
    
    forceExperienced = humanMass*deceleration
    print('force experienced is', forceExperienced)    
    
    timeForVT = terminalVelocity/gravity
    print('time for terminal velocity is', timeForVT)
    
    distanceForVT = 0.5*gravity*timeForVT**2
    print('distance for terminal velocity is', distanceForVT)
    
    maximumVelocityTime = 0
    if(dropHeight>distanceForVT):
        maximumVelocityTime = (dropHeight-distanceForVT)/terminalVelocity
        
    totalTime = timeForVT + maximumVelocityTime
    print('maximum velocity time is', maximumVelocityTime)
    print('total time is', totalTime)    
    
    aAxis = aAxis + bubblewrapThickness
    bAxis = bAxis + bubblewrapThickness
    print()
