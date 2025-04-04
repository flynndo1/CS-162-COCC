#Function 1
# Returns Area of Rectangle
def rect_area(l,w):
    """ Multiplies, length (l) time width (w) to find the area of the rectangle
        based of user inputted dimensions. written by Adam Fitzpatrick """
    return l * w
#Function 2
# Returns Surface Area of Rectangular Solid


# Request the dimension of a solid rectangular object

length = int(input("Enter the length of the the object as a integer: "))
width = int(input("Enter the width of the the object as a integer: "))
height = int(input("Enter the height of the the object as a integer: "))

print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", str(rect_surface_area(length, width, height)))
print("Area of the rectangle: " + str(rect_area(length, width)))
