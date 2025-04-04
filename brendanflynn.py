#Function 1
# Returns Area of Rectangle

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

length = int(input("Enter the length of the the object as a integer: "))
width = int(input("Enter the width of the the object as a integer: "))
height = int(input("Enter the height of the the object as a integer: "))

print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", str(rect_surface_area(length, width, height)))
print("Area of the rectangle: " + str(rect_area(length, width)))