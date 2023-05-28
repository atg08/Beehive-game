from __future__ import annotations
from threedeebeetree import Point
from ratio import *




LENGTH_OF_MIDDLE_LIST = 7

"""
            A function to reorder a given list that returns an ordered list in a way that when this list is passed through
            a BST, it will create a balanced BST in the ratio 1:7

            Args:
            - my_coordinate_list: list[Point]

            Raises:
            - 
            - 

            Returns:
            - list[Point] - an ordered listof points from the given input list
     
        """
def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:

    if len(my_coordinate_list) <= LENGTH_OF_MIDDLE_LIST:
        return my_coordinate_list
    
    temp_list : list[Point] = []
    octant_list : list[list[Point]] = [[] for _ in range(8)]

    temp_percentile_x , temp_percentile_y, temp_percentile_z = [Percentiles() for _ in range(3)]

    for point in my_coordinate_list:
            for i in range(3):
                [temp_percentile_x, temp_percentile_y, temp_percentile_z][i].add_point(point[i])

    ratio_list_x, ratio_list_y, ratio_list_z = [per.ratio(12.5, 12.5) for per in [temp_percentile_x, temp_percentile_y, temp_percentile_z]]

    intersect_list_x_y_z = intersection(list0 = ratio_list_x , list1 = ratio_list_y , list2 = ratio_list_z , ref_list = my_coordinate_list)

    if intersect_list_x_y_z != []:
        index_mid_point = len(intersect_list_x_y_z)//2
        mid_point : Point = intersect_list_x_y_z[index_mid_point]
    else:
        return my_coordinate_list

    temp_list.extend([mid_point])
    my_coordinate_list.remove(mid_point)

    for p in my_coordinate_list:
        checkthreedee = (p[0] < mid_point[0], p[1] < mid_point[1], p[2] < mid_point[2])
        index = 0
        for i in range(3):
            index += int(checkthreedee[i]) * 2**(2-i)
        octant_list[index].append(p)

    
    for i in range (len(octant_list)):
        temp_list.extend(make_ordering(octant_list[i]))

    return temp_list


"""
            Intersection method to find the points that are common in the 3 input lists of x, y and z, with reference to another list

            Args:
            - list0 : list[int]
            - list1 : list[int]
            - list2 : list[int]
            - ref_list : list[Point]

            Raises:
            - 
            - 

            Returns:
            - list[Point] - list of points that intersect

            Complexity:
            - Worst case: O(n), n : len(ref_list).
            - Best case: O(1).        
        """
def intersection(list0 : list[int], list1 : list[int] , list2 : list[int] , ref_list : list[Point]) -> list[Point]:
    inter_list : list[Point] = []
    for point in ref_list:
        if point[0] in list0 and point[1] in list1 and point[2] in list2:
            inter_list.append(point)

    return inter_list
 
