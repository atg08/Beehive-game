from __future__ import annotations
from threedeebeetree import Point
from ratio import *
from algorithms.mergesort import mergesort



LENGTH_OF_MIDDLE_LIST = 7

def intersection(list1 : list[Point], list2 : list[Point]) -> list[Point]:
    list3 = [value for value in list1 if value in list2]
    return list3

def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:

    if len(my_coordinate_list) <= LENGTH_OF_MIDDLE_LIST:
        return my_coordinate_list
    
    temp_list : list[Point] = []
    octant_list : list[list[Point]] = [[], [] , [] , [] , [] , [] , [] , []]

    temp_percentile_x , temp_percentile_y, temp_percentile_z = [Percentiles() for _ in range(3)]

    for point in my_coordinate_list:
            for i in range(3):
                [temp_percentile_x, temp_percentile_y, temp_percentile_z][i].add_point(point , input_key = lambda x : x[i])

    ratio_list_x, ratio_list_y, ratio_list_z = [per.ratio(12.5, 12.5) for per in [temp_percentile_x, temp_percentile_y, temp_percentile_z]]

    intersect_list_x_y_z = intersection(list1 = intersection(list1 = ratio_list_x , list2 = ratio_list_y) , list2 = ratio_list_z)

    if intersect_list_x_y_z != []:
        index_mid_point = len(intersect_list_x_y_z)//2
        mid_point : Point = intersect_list_x_y_z[index_mid_point]
    else:
        return my_coordinate_list

    temp_list.append(mid_point)

    index_mid_point = [per.my_pointy_tree.index(mid_point) for per in [temp_percentile_x, temp_percentile_y, temp_percentile_z]]

    for i in range (len(octant_list)):
        octant_list[i] = octanct_list_func(octant_index = i , perc1 = temp_percentile_x , perc2 = temp_percentile_y , perc3 = temp_percentile_z , index = index_mid_point)

    for i in range (len(octant_list)):
        temp_list.extend(make_ordering(octant_list[i]))

    return temp_list

def octanct_list_func(octant_index : int , perc1 : Percentiles , perc2 : Percentiles , perc3 : Percentiles , index : list[int]) -> list[Point]:
     match octant_index:
        case 0: 
            return intersection(list1 = intersection(list1 = perc1.my_pointy_tree[index[0] + 1:] , list2 = perc2.my_pointy_tree[index[1] + 1:]), list2 = perc3.my_pointy_tree[index[2] + 1:])
        case 1:
            return intersection(list1 = intersection(list1 = perc1.my_pointy_tree[:index[0]] , list2 = perc2.my_pointy_tree[index[1] + 1:]), list2 = perc3.my_pointy_tree[index[2] + 1:])
        case 2: 
            return intersection(list1 = intersection(list1 = perc1.my_pointy_tree[index[0] + 1:] , list2 = perc2.my_pointy_tree[:index[1]]), list2 = perc3.my_pointy_tree[index[2] + 1:])
        case 3:
            return intersection(list1 = intersection(list1 = perc1.my_pointy_tree[:index[0]] , list2 = perc2.my_pointy_tree[:index[1]]), list2 = perc3.my_pointy_tree[index[2] + 1:])
        case 4:
            return intersection(list1 = intersection(list1 = perc1.my_pointy_tree[index[0] + 1:] , list2 = perc2.my_pointy_tree[index[1] + 1:]), list2 = perc3.my_pointy_tree[:index[2]])
        case 5:
            return intersection(list1 = intersection(list1 = perc1.my_pointy_tree[:index[0]] , list2 = perc2.my_pointy_tree[index[1] + 1:]), list2 = perc3.my_pointy_tree[:index[2]])
        case 6:
            return intersection(list1 = intersection(list1 = perc1.my_pointy_tree[index[0] + 1:] , list2 = perc2.my_pointy_tree[:index[1]]), list2 = perc3.my_pointy_tree[:index[2]])
        case 7:
            return intersection(list1 = intersection(list1 = perc1.my_pointy_tree[:index[0]] , list2 = perc2.my_pointy_tree[:index[1]]), list2 = perc3.my_pointy_tree[:index[2]])
     
     
   
