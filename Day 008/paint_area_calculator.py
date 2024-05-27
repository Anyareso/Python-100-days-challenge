# Calculates cans of paint needed to paint a wall
# Given the height and width
import math
def paint_calc(height, width, cover):
    no_of_cans = (height * width)/cover
    rounded_no = math.ceil(no_of_cans)
    print(rounded_no)

test_h = int(input("Enter height of the wall in metres: "))
test_w = int(input("Enter width of the wall in metres: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)