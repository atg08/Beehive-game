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
        self.my_pointy_tree : BinarySearchTree[T , I] = BinarySearchTree()


    def add_point(self, item: T):
        self.my_pointy_tree[item] = item
    
    def remove_point(self, item: T):
        del self.my_pointy_tree[item]

    def ratio(self, x, y) -> list[T]:
        
        array = self.my_pointy_tree.get_sorted_array()

        lower_limit = math.ceil(len(self.my_pointy_tree)*(x/100))
        upper_limit = len(self.my_pointy_tree) - math.ceil(len(self.my_pointy_tree)*(y/100))

        temp_list : list[T] = []

        for node_index in range (lower_limit, upper_limit):
            temp_list.append(array[node_index])


        return temp_list


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
    p.remove_point(10)
    print(p.ratio(15, 66))
