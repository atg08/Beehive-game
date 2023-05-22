from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil
from bst import BinarySearchTree
import math
from algorithms.binary_search import binary_search

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        self.my_pointy_tree : list[T] = []


    def add_point(self, item: T):
        index = binary_search(l = self.my_pointy_tree , item = item , is_insert = True)
        self.my_pointy_tree.insert(index , item)
    

    def remove_point(self, item: T):
        index = binary_search(l = self.my_pointy_tree , item = item)
        del self.my_pointy_tree[index]
        

    def ratio(self, x, y) -> list[T]:
        lower_limit = math.ceil(len(self.my_pointy_tree)*(x/100))
        upper_limit = len(self.my_pointy_tree) - math.ceil(len(self.my_pointy_tree)*(y/100))

        #print("lower limit is " , lower_limit , "\nupper limit is " , upper_limit , "\nlength of tree is " , len(self.my_pointy_tree))
        temp_list : list[T] = []

        for node_index in range (lower_limit, upper_limit):
            temp_list.append(self.my_pointy_tree[node_index])


        return temp_list
    

    # def __init__(self) -> None:
    #     self.my_pointy_tree : BinarySearchTree[T , I] = BinarySearchTree()


    # def add_point(self, item: T):
    #     self.my_pointy_tree[item] = None
    
    # def remove_point(self, item: T):
    #     del self.my_pointy_tree[item]

    # def ratio(self, x, y) -> list[T]:
    #     lower_limit = math.ceil(len(self.my_pointy_tree)*(x/100))
    #     upper_limit = len(self.my_pointy_tree) - math.ceil(len(self.my_pointy_tree)*(y/100))

    #     #print("lower limit is " , lower_limit , "\nupper limit is " , upper_limit , "\nlength of tree is " , len(self.my_pointy_tree))
    #     temp_list : list[T] = []

    #     for node_index in range (lower_limit + 1 , upper_limit + 1):
    #         temp_list.append(self.my_pointy_tree.kth_smallest(k = node_index , current = self.my_pointy_tree.root).key)


    #     return temp_list

        


if __name__ == "__main__":
    points = list(range(50))
    import random
    random.shuffle(points)
    print(points, "\n")
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # p.my_pointy_tree.draw()
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))
