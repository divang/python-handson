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
