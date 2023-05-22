from __future__ import annotations
from typing import Generic, TypeVar, Tuple
from dataclasses import dataclass, field
from referential_array import ArrayR

I = TypeVar('I')
Point = Tuple[int, int, int]


def get_octant(reference_key : Point , input_key : Point) -> int:
      
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
    
    """
    my_child[0] = top north-east (+++)
    my_child[1] = top north-west (-++)
    my_child[2] = top south-east (+-+)
    my_child[3] = top south-west (--+)
    my_child[4] = bot north-east (++-)
    my_child[5] = bot north-west (-+-)
    my_child[6] = bot south-east (+--)
    my_child[7] = bot south-west (---)
    """
    subtree_size: int = 1

    def __init__(self, key : Point, item : I) -> None:
          self.key = key
          self.item = item
          self.my_child = ArrayR(length = 8)
          for i in range (len(self.my_child)):
                self.my_child[i] = None
                

    def get_child_for_key(self, point: Point) -> BeeNode | None:
          octant = get_octant(reference_key = self.key , input_key = point)
          return self.my_child[octant]
          


class ThreeDeeBeeTree(Generic[I]):
    """ 3️⃣🇩🐝🌳 tree. """

    def __init__(self) -> None:
        """
            Initialises an empty 3DBT
        """
        self.root : BeeNode|None = None
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

        return self.get_tree_node_by_key_aux(current = self.root ,key = key)
    
    def get_tree_node_by_key_aux(self, current : BeeNode , key : Point) -> BeeNode:

        if current is None:
            raise KeyError('Key not found: {0}'.format(key))
        elif current.key == key:
            return current
        else:
            octant = get_octant(reference_key = current.key , input_key = key)
            return self.get_tree_node_by_key_aux(current = current.my_child[octant] , key = key )
            


    def __setitem__(self, key: Point, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BeeNode, key: Point, item: I) -> BeeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
        """

        if current is None:
            current = BeeNode(key = key , item = item)
            self.length += 1
        elif current.key == key:
            raise ValueError("Key already exists")
        else:
            octant = get_octant(reference_key = current.key , input_key = key)
            current.my_child[octant] = self.insert_aux(current = current.my_child[octant] , key = key , item = item)
            current.subtree_size += 1
        return current

        

    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """
        return current.subtree_size == 1
    


if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size) # 2
