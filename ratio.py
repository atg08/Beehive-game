from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil
from bst import BinarySearchTree

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        self.BST = BinarySearchTree()
        
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
            - Worst case: O(log) n : the number of nodes.
        """
        self.BST[item] = None
        
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
        del self.BST[item]

    def ratio(self, x, y): # 13, 10
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
            - Worst case: O(log n + O) : n, the total number of points. O, the number of points returned by function.
        """
        x_ratio = ceil(x / 100 * len(self.BST)) + 1
        y_ratio = len(self.BST) - ceil(y / 100 * len(self.BST))

        temp_list = []

        for i in range(x_ratio,y_ratio + 1):
            temp_list.append(self.BST.kth_smallest(i,self.BST.root).key)

        return temp_list
        

if __name__ == "__main__":
    points = list(range(50))
    import random
    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))
