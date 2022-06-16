# This is a python comment single line
# How to run this code
# Save to a indentation-example.py
# First block of the code i.e Calculate Rectangle area [2 arguments]
# python  indentation-example.py 10 20 
# Second block of the code i.e Calculate Circle area [1 argument]
# python  indentation-example.py 10 

import sys
print("Hello!!")
print(sys.argv)

if len(sys.argv) > 2:
   x_dim = sys.argv[1]
   y_dim = sys.argv[2]
   # It is a rectangle and now calculating the area of rectangle
   rec_area = int(x_dim) * int(y_dim)
   print("Area of Rectangle:")
   print(rec_area)
else:
   # It is circle and now calculating area of circle
   radius = sys.argv[1]
   r = int(radius)
   pi = 3.14
   circle_area = pi * r * r
   print("Area of Circle:")
   print(circle_area)
