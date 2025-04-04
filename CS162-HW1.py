#Function 1
# Returns Area of Rectangle
def rect_area(l,w):
    """ Multiplies, length (l) time width (w) to find the area of the rectangle
        based of user inputted dimensions. written by Adam Fitzpatrick """
    return l * w

#Function 2
# Returns Surface Area of Rectangular Solid
def rect_surface_area (l,w,h):
    """Calculates the surface area of a rectangular solid given the length(l), width(w), and height(h). Written by Brendan Flynn"""
    # The surface area of a rectangular solid is given by 2*(l*w + l*h + w*h)
    area_1 = rect_area(l,w)
    area_2 = rect_area(l,h)
    area_3 = rect_area(w,h)

    return 2 * (area_1 + area_2 + area_3)

# Request the dimension of a solid rectangular object

l = int(input("Enter the length of the the object as a integer: "))
w = int(input("Enter the width of the the object as a integer: "))
h = int(input("Enter the height of the the object as a integer: "))

print("Length = ", l, "Width = ", w, "Height = ", h)
print("Total Surface Area = ", str(rect_surface_area(l, w, h)))
print("Area of the rectangle: " + str(rect_area(l, w)))
