import math 

def rhombus_area(side ,height):
    area = side * height
    return area


side = float(input("Enter side of rhombus :"))
height = float(input("Enter height of rhombus :"))
area = rhombus_area(side,height)
print(f'{area} cm sq.')

def rhombus_area_diagonals(diagonal1,diagonal2):
    area = (diagonal1 * diagonal2)/2
    return area


diagonal1 = float(input("Enter Diagonal one :"))
diagonal2 = float(input("Enter Diagonal two :"))

area = rhombus_area_diagonals(diagonal1,diagonal2)
print(f'{area} cm sq.')
