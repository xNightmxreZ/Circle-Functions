#Isiah Williams

import Circle
import math

def main():
  print("Menu of available functions: ") 
  print("1 - Circumference")
  print("2 - Area")
  print("3 - Arc")
  print("4 - Sector: Perimeter")
  print("5 - Sector: Area")
  print("6 - Chord")
  print("7 - Segment: Perimeter")
  print("8 - Segment: Area")

main()
choice = int(input("Please enter your menu Choice: "))

if choice == 1:
  radius = float(input("Please enter the radius: "))
    
  print(f"The circumference of a circle with a radius of {radius:.2f} is {Circle.circumference(radius):.2f}")
  
elif choice == 2:
  radius = float(input("Please enter the radius: "))
    
  print(f"The area of a circle with a radius of {radius:.2f} is {Circle.area(radius):.2f}")
    
elif choice == 3:
  radius = float(input("Please enter the radius: "))
  angle = float(input("Please enter the angle: "))
    
  print(f"The arc length of a circle with a radius of {radius:.2f} and an angle of {angle:.2f} is {Circle.arc(radius, angle):.2f}")
  
elif choice == 4:
  radius = float(input("Please enter the radius: "))
  angle = float(input("Please enter the angle: "))
    
  print(f"The sector perimeter of a circle with a radius of {radius:.2f} and an angle of {angle:.2f} is {Circle.secperimeter(radius, angle):.2f}")

elif choice == 5:
  radius = float(input("Please enter the radius: "))
  angle = float(input("Please enter the angle: "))
    
  print(f"The sector area of a circle with a radius of {radius:.2f} and an angle of {angle:.2f} is {Circle.secarea(radius, angle):.2f}")
   
elif choice == 6:
  radius = float(input("Please enter the radius: "))
  angle = float(input("Please enter the angle: "))
    
  print(f"The chord of a circle with a radius of {radius:.2f} and an angle of {angle:.2f} is {Circle.chord(radius, angle):.2f}")
   
elif choice == 7:
  radius = float(input("Please enter the radius: "))
  angle = float(input("Please enter the angle: "))
    
  print(f"The perimeter of a segment of a circle with a radius of {radius:.2f} and an angle of {angle:.2f} is {Circle.segperimeter(radius, angle):.2f}")

elif choice == 8:
  radius = float(input("Please enter the radius: "))
  angle = float(input("Please enter the angle: "))
    
  print(f"The area of a segment of a circle with a radius of {radius:.2f} and an angle of {angle:.2f} is {Circle.segarea(radius, angle):.2f}")

else:
  print("Please choose a valid input")