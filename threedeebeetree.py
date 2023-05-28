from __future__ import annotations
from typing import Generic, TypeVar, Tuple
from dataclasses import dataclass, field
from referential_array import ArrayR

I = TypeVar('I')
Point = Tuple[int, int, int]
NUMBER_OF_CHILDREN = 8

def get_octant(reference_key : Point, input_key : Point) -> int:
    """
        Get the correct space between 8 (x,y,z axis)

        Args:
        - reference_key : Tuple[int, int, int]
        - input_key : Tuple[int, int, int]

        Raises:
        - 
        - 

        Returns:
        - return betwen 0 ~ 7

        Complexity:
        - O(1)   
    """

    if input_key[2] >= reference_key[2] and input_key[1] >= reference_key[1] and input_key[0] >= reference_key[0]: 
        return 0
    elif input_key[2] >= reference_key[2] and input_key[1] >= reference_key[1] and input_key[0] < reference_key[0]: 
        return 1
    elif input_key[2] >= reference_key[2] and input_key[1] < reference_key[1] and input_key[0] >= reference_key[0]: 
        return 2
    elif input_key[2] >= reference_key[2] and input_key[1] < reference_key[1] and input_key[0] < reference_key[0]: 
        return 3
    elif input_key[2] < reference_key[2] and input_key[1] >= reference_key[1] and input_key[0] >= reference_key[0]: 
        return 4
    elif input_key[2] < reference_key[2] and input_key[1] >= reference_key[1] and input_key[0] < reference_key[0]: 
        return 5
    elif input_key[2] < reference_key[2] and input_key[1] < reference_key[1] and input_key[0] >= reference_key[0]: 
        return 6
    elif input_key[2] < reference_key[2] and input_key[1] < reference_key[1] and input_key[0] < reference_key[0]: 
        return 7
      
@dataclass
class BeeNode:
    
    key: Point
    my_child : ArrayR[BeeNode] 
    item: I = None
    
    subtree_size: int = 1

    def __init__(self, key : Point, item : I) -> None:
        self.key = key
        self.item = item
        self.my_child = ArrayR(length = NUMBER_OF_CHILDREN)
        for i in range (len(self.my_child)):
            self.my_child[i] = None
                
    def get_child_for_key(self, point: Point) -> BeeNode | None:
        octant_item = get_octant(reference_key = self.key, input_key = point)
        return self.my_child[octant_item]



class ThreeDeeBeeTree(Generic[I]):
    """ 3️⃣🇩🐝🌳 tree. """

    def __init__(self) -> None:
        """
            Initialises an empty 3DBT
        """
        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the 3DBT is empty
        """
        return len(self) == 0

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: Point) -> bool:
        """
            Checks to see if the key is in the 3DBT
        """
        try:
            self.get_tree_node_by_key(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key: Point) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
        """
        node = self.get_tree_node_by_key(key)
        return node.item

    def get_tree_node_by_key(self, key: Point) -> BeeNode:
        return self.get_tree_node_by_key_aux(current= self.root, key = key)
    
    def get_tree_node_by_key_aux(self, current: BeeNode, key = Point) -> BeeNode:
        """
            Attempts to get treenode through key.

            Args:
            - current : Beenode.
            - key: Point.
            
            Raises:
            - ValueError : when the key is not in current.
            - 

            Returns:
            - Beenode : Beenode.

            Complexity:
            - Best case: O(1)
            - Worst case: O(log n + O) : n, the total number of points. O, the number of points returned by function.
        """

        if current is None:
            raise ValueError ("Key is None !")
        elif current.key == key:
            return current
        else:
            octant_value = get_octant(reference_key = current.key , input_key = key)
            return self.get_tree_node_by_key_aux(current = current.my_child[octant_value], key = key)


    def __setitem__(self, key: Point, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BeeNode, key: Point, item: I) -> BeeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it

            Args:
            - current : Beenode.
            - key : Point
            - item : item
            
            Raises:
            - ValueError : when the key is not in current. 

            Returns:
            - current : Beenode.

            Complexity:
            - Best & Worst case: O(D) : Depth of beenode.
        """
        
        if current is None:
            current = BeeNode(key = key , item = item)
            self.length += 1
        elif current.key == key:
            raise ValueError("Key already exist.")
        else:
            octant_value = get_octant(reference_key = current.key , input_key = key)
            current.my_child[octant_value] = self.insert_aux(current = current.my_child[octant_value], key = key, item = item )
            current.subtree_size += 1

        return current

    def is_leaf(self, current: BeeNode) -> bool:
        """ 
            Simple check whether or not the node is a leaf. 
        
            Args:
            - current : Beenode.
            
            Returns:
            - Boolean : current node is leaf or not.

            Complexity:
            - Best & Worst case: O(1)
        """
        return current.subtree_size == 1


if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size) # 2
