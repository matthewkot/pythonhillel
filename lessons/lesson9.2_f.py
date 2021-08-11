import random

def create_point(min_limit,max_limit):
    point = {"x": random.randint(-10, 10),
             "y": random.randint(-10, 10)}
    return point

def create_triangle(points_name_str, min_limit, max_limit) :
    return {key: create_point(-100,100) for key in points_name_str}

triangle_ABC = create_triangle("ABC", -100,100)
triangle_MNK = create_triangle("MNK", -100,100)
triangle_QWE = create_triangle("QWE",-100,100)


print(triangle_ABC)
print(triangle_MNK)
print(triangle_QWE)


# point_A = create_point()
# point_B = create_point()
# point_C = create_point()

# triangle_ABC = {"A": create_point(),
#                 "B": create_point(),
#                 "C": create_point()}

# triangle_ABC = {key: create_point() for key in "ABC"} ### Второй метод



# def create_triangle():                            ### Третий (самый короткий) метод
#     return {key: create_point() for key in "ABC"}
#
# triangle_ABC = create_triangle()



# def create_triangle(points_name_str):
#     return {key: create_point() for key in points_name_str}


# triangle_ABC = create_triangle("ABC")
# triangle_MNK = create_triangle("MNK")
# triangle_QWE = create_triangle("QWE")
#
#
# print(triangle_ABC)
# print(triangle_MNK)
# print(triangle_QWE)