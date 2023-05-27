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
    
    # temp_percentile_x : Percentiles[Point] = Percentiles()
    # temp_percentile_y : Percentiles[Point] = Percentiles()
    # temp_percentile_z : Percentiles[Point] = Percentiles()

    for point in my_coordinate_list:
            for i in range(3):
                [temp_percentile_x, temp_percentile_y, temp_percentile_z][i].add_point(point , input_key = lambda x : x[i])


    # for point in my_coordinate_list:
    #     temp_percentile_x.add_point(point , input_key = lambda x : x[0])
    #     temp_percentile_y.add_point(point , input_key = lambda x : x[1])
    #     temp_percentile_z.add_point(point , input_key = lambda x : x[2])

    ratio_list_x, ratio_list_y, ratio_list_z = [per.ratio(12.5, 12.5) for per in [temp_percentile_x, temp_percentile_y, temp_percentile_z]]

    # ratio_list_x = temp_percentile_x.ratio(12.5 , 12.5)
    # ratio_list_y = temp_percentile_y.ratio(12.5 , 12.5)
    # ratio_list_z = temp_percentile_z.ratio(12.5 , 12.5)

    intersect_list_x_y_z = intersection(list1 = intersection(list1 = ratio_list_x , list2 = ratio_list_y) , list2 = ratio_list_z)


    if intersect_list_x_y_z != []:
        index_mid_point = len(intersect_list_x_y_z)//2
        mid_point : Point = intersect_list_x_y_z[index_mid_point]
    else:
        return my_coordinate_list


    temp_list.append(mid_point)
    index_mid_point_x = temp_percentile_x.my_pointy_tree.index(mid_point)
    index_mid_point_y = temp_percentile_y.my_pointy_tree.index(mid_point)
    index_mid_point_z = temp_percentile_z.my_pointy_tree.index(mid_point)

    octant_list[0] = (intersection(list1 = intersection(list1 = temp_percentile_x.my_pointy_tree[index_mid_point_x + 1:] , list2 = temp_percentile_y.my_pointy_tree[index_mid_point_y + 1:]), list2 = temp_percentile_z.my_pointy_tree[index_mid_point_z + 1:]))
    octant_list[1] = (intersection(list1 = intersection(list1 = temp_percentile_x.my_pointy_tree[:index_mid_point_x] , list2 = temp_percentile_y.my_pointy_tree[index_mid_point_y + 1:]), list2 = temp_percentile_z.my_pointy_tree[index_mid_point_z + 1:]))
    octant_list[2] = (intersection(list1 = intersection(list1 = temp_percentile_x.my_pointy_tree[index_mid_point_x + 1:] , list2 = temp_percentile_y.my_pointy_tree[:index_mid_point_y]), list2 = temp_percentile_z.my_pointy_tree[index_mid_point_z + 1:]))
    octant_list[3] = (intersection(list1 = intersection(list1 = temp_percentile_x.my_pointy_tree[:index_mid_point_x] , list2 = temp_percentile_y.my_pointy_tree[:index_mid_point_y]), list2 = temp_percentile_z.my_pointy_tree[index_mid_point_z + 1:]))
    octant_list[4] = (intersection(list1 = intersection(list1 = temp_percentile_x.my_pointy_tree[index_mid_point_x + 1:] , list2 = temp_percentile_y.my_pointy_tree[index_mid_point_y + 1:]), list2 = temp_percentile_z.my_pointy_tree[:index_mid_point_z]))
    octant_list[5] = (intersection(list1 = intersection(list1 = temp_percentile_x.my_pointy_tree[:index_mid_point_x] , list2 = temp_percentile_y.my_pointy_tree[index_mid_point_y + 1:]), list2 = temp_percentile_z.my_pointy_tree[:index_mid_point_z]))
    octant_list[6] = (intersection(list1 = intersection(list1 = temp_percentile_x.my_pointy_tree[index_mid_point_x + 1:] , list2 = temp_percentile_y.my_pointy_tree[:index_mid_point_y]), list2 = temp_percentile_z.my_pointy_tree[:index_mid_point_z]))
    octant_list[7] = (intersection(list1 = intersection(list1 = temp_percentile_x.my_pointy_tree[:index_mid_point_x] , list2 = temp_percentile_y.my_pointy_tree[:index_mid_point_y]), list2 = temp_percentile_z.my_pointy_tree[:index_mid_point_z]))

    for i in range (len(octant_list)):
        temp_list.extend(make_ordering(octant_list[i]))

    return temp_list
   

    


    


    

   




    # if len(my_coordinate_list) <= LENGTH_OF_MIDDLE_LIST:
    #     return my_coordinate_list
    
    
    # temp_list = []
    # temp_percentile : Percentiles[Point] = Percentiles()
    # for point in my_coordinate_list:
    #     temp_percentile.add_point(point)

    # limit = (len(my_coordinate_list) - LENGTH_OF_MIDDLE_LIST)/2
    # percentage_limit = (limit * 100)/len(my_coordinate_list)


    # # print("\nlimit is " , limit , " and perct limit is " , percentage_limit)

    # # print("temp list before middle list " , temp_list ,  " \nand length of list is " , len(temp_list))
    # temp_list.extend(temp_percentile.ratio(percentage_limit , percentage_limit))

    # left_index = math.ceil((len(my_coordinate_list) * (percentage_limit)) / 100)
    # # print("temp list before left list " , temp_list , " \nand length of list is " , len(temp_list))
    # temp_list.extend(make_ordering(temp_percentile.my_pointy_tree[0 : left_index]))

    # right_index = len(my_coordinate_list) - math.ceil(((percentage_limit * len(my_coordinate_list)) / 100))
    
    # # print("temp list before right list " , temp_list ,  " \nand length of list is " , len(temp_list))
    # temp_list.extend(make_ordering(temp_percentile.my_pointy_tree[right_index : len(my_coordinate_list)]))
    # # print("temp list after " , temp_list,  " \nand length of list is " , len(temp_list))
    # return temp_list
    


