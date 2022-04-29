'''This library has all the functions found at: 
https://www.101computing.net/circle-geometry-functions/
'''
import math

def circumference(rad):
  return (2 * math.pi * rad)

def area(rad):
  return (math.pi * rad ** 2)
  
def arc(rad, angle):
  return (2 * math.pi * rad * (angle/360))
  
def secperimeter(rad, angle):
  return ((2 * math.pi * (angle/360) + 2 * rad))
  
def secarea(rad, angle):
  return (math.pi * (rad ** 2) * (angle/360))
  
def chord(rad, angle):
  return (2 * rad * math.sin((angle/2)))
  
def segperimeter(rad, angle):
  return (2 * math.pi * (angle/360) + 2 * rad * math.sin(angle/360))
  
def segarea(rad, angle):
  return (rad ** 2 * (math.pi * (angle/360) - 0.5 * math.sin(angle)))