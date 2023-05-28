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
        """
            Adds a point to the object.

            Args:
            - item : item

            Raises:
            - 
            - 

            Returns:
            - 

            Complexity:
            - Best case: O(1)
            - Worst case: O(log n) : the number of nodes.
        """
        self.my_pointy_tree[item] = item
    
    def remove_point(self, item: T):
        """
            Removes a point from the object.

            Args:
            - item : item

            Raises:
            - 
            - 

            Returns:
            - 

            Complexity:
            - Best case: O(1)
            - Worst case: O(log n) : the number of nodes.
        """
        del self.my_pointy_tree[item]

    def ratio(self, x, y) -> list[T]:
        """
            Computes a list of all items fitting the larger than/smaller than criteria.
             This list doesn't need to be sorted.

            Args:
            - x : Larger than at least x% of the elements in the list.
            - y : Smaller than at least y% of the elements in the list.
            
            Raises:
            - 
            - 

            Returns:
            - list : list based on the (x,y) ratio.

            Complexity:
            - Best case: O(1)
            - Worst case: O(log n * O) : n, the total number of points. O, the number of points returned by function.
        """
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
