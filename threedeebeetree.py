from __future__ import annotations
from typing import Generic, TypeVar, Tuple
from dataclasses import dataclass, field
from referential_array import ArrayR

I = TypeVar('I')
Point = Tuple[int, int, int]

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
        print("point is " , point)
        for child in range (len(self.my_child)):
            if self.my_child[child] != None:
                match child:
                    case 0:
                            if point[2] >= self.key[2] and point[1] >= self.key[1] and point[0] >= self.key[0]:
                                print("\nmy child is " , self.my_child[child].key)
                                return self.my_child[child]
                    case 1:
                            if point[2] >= self.key[2] and point[1] >= self.key[1] and point[0] < self.key[0]:
                                print("\nmy child is " , self.my_child[child].key)
                                return self.my_child[child]
                    case 2:
                            if point[2] >= self.key[2] and point[1] < self.key[1] and point[0] >= self.key[0]:
                                print("\nmy child is " , self.my_child[child].key)
                                return self.my_child[child]
                    case 3:
                            if point[2] >= self.key[2] and point[1] < self.key[1] and point[0] < self.key[0]:
                                print("\nmy child is " , self.my_child[child].key)
                                return self.my_child[child]
                    case 4:
                            if point[2] < self.key[2] and point[1] >= self.key[1] and point[0] >= self.key[0]:
                                print("\nmy child is " , self.my_child[child].key)
                                return self.my_child[child]
                    case 5:
                            if point[2] < self.key[2] and point[1] >= self.key[1] and point[0] < self.key[0]:
                                print("\nmy child is " , self.my_child[child].key)
                                return self.my_child[child]
                    case 6:
                            if point[2] < self.key[2] and point[1] < self.key[1] and point[0] >= self.key[0]:
                                print("\nmy child is " , self.my_child[child].key)
                                return self.my_child[child]
                    case 7:
                            if point[2] < self.key[2] and point[1] < self.key[1] and point[0] < self.key[0]:
                                print("\nmy child is " , self.my_child[child].key)
                                return self.my_child[child]                          
        return None


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
        raise NotImplementedError()

    def __setitem__(self, key: Point, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BeeNode, key: Point, item: I) -> BeeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
        """

        #temp_node : BeeNode = None
        if current is None:
            current = BeeNode(key = key , item = item)
            print("current id " , id(current.my_child))
            self.length += 1
        elif key[2] >= current.key[2] and key[1] >= current.key[1] and key[0] >= current.key[0]: 
                    current.my_child[0] = self.insert_aux(current = current.my_child[0], key = key, item = item)
                    current.subtree_size += 1
        elif key[2] >= current.key[2] and key[1] >= current.key[1] and key[0] < current.key[0]: 
                    current.my_child[1] = self.insert_aux(current.my_child[1], key, item)
                    # current.my_child[1] = temp_node
                    current.subtree_size += 1
        elif key[2] >= current.key[2] and key[1] < current.key[1] and key[0] >= current.key[0]: 
                    current.my_child[2] = self.insert_aux(current = current.my_child[2], key = key, item = item) 
                    current.subtree_size += 1 
        elif key[2] >= current.key[2] and key[1] < current.key[1] and key[0] < current.key[0]: 
                    current.my_child[3] = self.insert_aux(current = current.my_child[3], key = key, item = item)
                    current.subtree_size += 1 
        elif key[2] < current.key[2] and key[1] >= current.key[1] and key[0] >= current.key[0]: 
                    current.my_child[4] = self.insert_aux(current = current.my_child[4], key = key, item = item) 
                    current.subtree_size += 1
        elif key[2] < current.key[2] and key[1] >= current.key[1] and key[0] < current.key[0]: 
                    current.my_child[5] = self.insert_aux(current = current.my_child[5], key = key, item = item)
                    current.subtree_size += 1
        elif key[2] < current.key[2] and key[1] < current.key[1] and key[0] >= current.key[0]: 
                    current.my_child[6] = self.insert_aux(current = current.my_child[6], key = key, item = item)
                    current.subtree_size += 1
        elif key[2] < current.key[2] and key[1] < current.key[1] and key[0] < current.key[0]: 
                    current.my_child[7] = self.insert_aux(current = current.my_child[7], key = key, item = item)
                    current.subtree_size += 1
        else:
            return ValueError("Key already exists")
        return current
    
        # if current is None:
        #     current = BeeNode(key = key , item = item)
        # if key[2] > current.key[2]:
        #     if key[1] > current.key[1]:
        #         if key[0] > current.key[0]: 
        #             current.my_child[0] = self.insert_aux(current = current.my_child[0], key = key, item = item)
        #         else:
        #             current.my_child[1] = self.insert_aux(current = current.my_child[1], key = key, item = item)
        #     else:
        #         if key[0] > current.key[0]:
        #             current.my_child[2] = self.insert_aux(current = current.my_child[2], key = key, item = item)
        #         else:
        #             current.my_child[3] = self.insert_aux(current = current.my_child[3], key = key, item = item)
        # elif key[2] < current.key[2]:
        #     if key[1] > current.key[1]:
        #         if key[0] > current.key[0]:
        #             current.my_child[4] = self.insert_aux(current = current.my_child[4], key = key, item = item)
        #         else:
        #             current.my_child[5] = self.insert_aux(current = current.my_child[5], key = key, item = item)
        #     else:
        #         if key[0] > current.key[0]:
        #             current.my_child[6] = self.insert_aux(current = current.my_child[6], key = key, item = item)
        #         else:
        #             current.my_child[7] = self.insert_aux(current = current.my_child[7], key = key, item = item)
        # else:
        #     return ValueError("key already exists")
        # return current






        # raise NotImplementedError()

    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """
        raise NotImplementedError()

if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size) # 2
