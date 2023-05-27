from __future__ import annotations
from threedeebeetree import Point
from ratio import *

def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    
    lst = []

    if len(my_coordinate_list) <= 17:
        return my_coordinate_list

    else:
        per_x, per_y, per_z = [Percentiles() for _ in range(3)]

        for point in my_coordinate_list:
            for i in range(3):
                [per_x, per_y, per_z][i].add_point(point[i])
            
        select_x, select_y, select_z = [per.ratio(12.5, 12.5) for per in [per_x, per_y, per_z]]

        children_list = [[], [], [], [], [], [], [], []]

        for p in my_coordinate_list:
            if p[0] in select_x and p[1] in select_y and p[2] in select_z:
                checkpoint = p
                lst.append(checkpoint)
                my_coordinate_list.remove(checkpoint)
                break
        
        for p in my_coordinate_list:
            checkthreedee = (p[0] < checkpoint[0], p[1] < checkpoint[1], p[2] < checkpoint[2])
            index = 0
            for i in range(3):
                index += int(checkthreedee[i]) * 2**(2-i)
            children_list[index].append(p)

        for child in children_list:
            lst.extend(make_ordering(child))

        return lst
