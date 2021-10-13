
def minimum_bounding_box(shapes):
    shapes_in_array = shapes.split(',')
    shapes_formatted = []
    for shape in shapes_in_array:
        shapes_formatted.append(shape.split())
    
    first = int(shapes_formatted[0][1]) + int(shapes_formatted[1][1]) 
    second = int(shapes_formatted[1][1]) + int(shapes_formatted[2][2])
    return f"{first} {second}"

if __name__ == '__main__':
    teste = "circle 15, square 20, rectangle 35 10"

    result = minimum_bounding_box(teste)
    print(result)