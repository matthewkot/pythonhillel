import random

MIN_LIMIT = -10
MAX_LIMIT = 10


def create_point(min_limit = MIN_LIMIT,max_limit = MAX_LIMIT):
    point = {"x": random.randint(min_limit, max_limit),
             "y": random.randint(min_limit, max_limit)}
    return point

def create_triangle(points_name_str ) :
    return {key: create_point() for key in points_name_str}

def print_triangle_list(triangle_list):
    print("-------------------------------------------------------------------------------")
    for triangle in triangle_list:
        print(triangle)
        print("-------------------------------------------------------------------------------")


triangle_list = []
names = ["ABC", "MNK", "QWE", "ZSD"]
for name in names:
    triangle = create_triangle(name)
    triangle_list.append(triangle)

print_triangle_list(triangle_list)





# triangle_ABC = create_triangle("ABC" )
# triangle_MNK = create_triangle("MNK")
# triangle_QWE = create_triangle("QWE")
#
#
# print(triangle_ABC)
# print(triangle_MNK)
# print(triangle_QWE)