""" Binary Search Tree ADT.
    Defines a Binary Search Tree with linked nodes.
    Each node contains a key and item as well as references to the children.
"""

from __future__ import annotations

__author__ = 'Brendon Taylor, modified by Alexey Ignatiev, further modified by Jackson Goerner'
__docformat__ = 'reStructuredText'

from typing import TypeVar, Generic
from node import TreeNode
import sys
from referential_array import ArrayR


# generic types
K = TypeVar('K')
I = TypeVar('I')
T = TypeVar('T')


class BinarySearchTree(Generic[K, I]):
    """ Basic binary search tree. """

    def __init__(self) -> None:
        """
            Initialises an empty Binary Search Tree
            :complexity: O(1)
        """

        self.root : TreeNode[K,I]|None = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the bst is empty
            :complexity: O(1)
        """
        return self.root is None

    def __len__(self) -> int:
        """ 
            Returns the number of nodes in the tree.
            :complexity: O(1)
        """
        return self.length

    def __contains__(self, key: K) -> bool:
        """
            Checks to see if the key is in the BST
            :complexity: see __getitem__(self, key: K) -> (K, I)
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: K) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
            :complexity best: O(CompK) finds the item in the root of the tree
            :complexity worst: O(CompK * D) item is not found, where D is the depth of the tree
            CompK is the complexity of comparing the keys
        """
        return self.get_tree_node_by_key(key).item

    def get_tree_node_by_key(self, key: K) -> TreeNode:
        return self.get_tree_node_by_key_aux(self.root, key)

    def get_tree_node_by_key_aux(self, current: TreeNode, key: K) -> TreeNode:
        if current is None:
            raise KeyError('Key not found: {0}'.format(key))
        elif key == current.key:
            return current
        elif key < current.key:
            return self.get_tree_node_by_key_aux(current.left, key)
        else:  # key > current.key
            return self.get_tree_node_by_key_aux(current.right, key)

    def __setitem__(self, key: K, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: TreeNode, key: K, item: I) -> TreeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
            :complexity best: O(CompK) inserts the item at the root.
            :complexity worst: O(CompK * D) inserting at the bottom of the tree
            where D is the depth of the tree
            CompK is the complexity of comparing the keys
        """
        if current is None:  # base case: at the leaf
            current = TreeNode(key, item=item)
            self.length += 1
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, item)
            current.subtree_size += 1
        elif key > current.key:
            current.right = self.insert_aux(current.right, key, item)
            current.subtree_size += 1
        else:  # key == current.key
            raise ValueError('Inserting duplicate item')
        return current

    def __delitem__(self, key: K) -> None:
        self.root = self.delete_aux(self.root, key)

    def delete_aux(self, current: TreeNode, key: K) -> TreeNode:
        """
            Attempts to delete an item from the tree, it uses the Key to
            determine the node to delete.
            :complexity best: O(CompK) deletes the item at the root.
            :complexity worst: O(CompK * D) deleting at the bottom of the tree
            where D is the depth of the tree
            CompK is the complexity of comparing the keys
        """

        if current is None:  # key not found
            raise ValueError('Deleting non-existent item')
        elif key < current.key:
            current.left  = self.delete_aux(current.left, key)
            current.subtree_size -= 1
        elif key > current.key:
            current.right = self.delete_aux(current.right, key)
            current.subtree_size -= 1
        else:  # we found our key => do actual deletion
            if self.is_leaf(current):
                self.length -= 1
                return None
            elif current.left is None:
                self.length -= 1
                return current.right
            elif current.right is None:
                self.length -= 1
                return current.left

            # general case => find a successor
            succ = self.get_successor(current)
            current.key  = succ.key
            current.item = succ.item
            current.right = self.delete_aux(current.right, succ.key)
            current.subtree_size -= 1
            

        return current

    def get_successor(self, current: TreeNode) -> TreeNode:
        """
            Get successor of the current node.
            It should be a child node having the smallest key among all the larger keys.

            Args:
            - current: current Treenode

            Returns:
            - result: given some subtree node current, the smallest key node in the subtree rooted at current.

            Complexity:
            - Worst case: O(traverse_left)
            - Best case: O(1) 
        """

        if current.right == None:
            return None
        elif current.right.left == None:
                return current.right
        else:
            return self.traverse_left(current = current.right.left)
    


    def get_minimal(self, current: TreeNode) -> TreeNode:
        """
            Get a node having the smallest key in the current sub-tree.

            Args:
            - current: current Treenode

            Raises:
            - 
            - 

            Returns:
            - result: treenode that is the smallest key node in the subtree rooted at current.

            Complexity:
            - Best & Worst case: O(traverse_left)
        """
        return self.traverse_left(current = current)
    
    
    def traverse_left(self , current : TreeNode) -> TreeNode:
        """
            Traversing the left subnode of current node.

            Args:
            - current: current Treenode

            Raises:
            - 
            - 

            Returns:
            - result: treenode that is the smallest key node in the subtree rooted at current.

            Complexity:
            - Worst case: O(n), n : the number of nodes.
            - Best case: O(1)
        """
        if current.left == None:
            return current  
     
        return self.traverse_left(current = current.left)


    def is_leaf(self, current: TreeNode) -> bool:
        """ 
        Simple check whether or not the node is a leaf. 
        
        - Worst case : O(1)
        - Best case : O(1)
        """

        return current.left is None and current.right is None

    def draw(self, to=sys.stdout):
        """ Draw the tree in the terminal. """

        # get the nodes of the graph to draw recursively
        self.draw_aux(self.root, prefix='', final='', to=to)

    def draw_aux(self, current: TreeNode, prefix='', final='', to=sys.stdout) -> K:
        """ Draw a node and then its children. """

        if current is not None:
            real_prefix = prefix[:-2] + final
            print('{0}{1} , {2}'.format(real_prefix, str(current.key) , str(current.item)), file=to)

            if current.left or current.right:
                self.draw_aux(current.left,  prefix=prefix + '\u2551 ', final='\u255f\u2500', to=to)
                self.draw_aux(current.right, prefix=prefix + '  ', final='\u2559\u2500', to=to)
        else:
            real_prefix = prefix[:-2] + final
            print('{0}'.format(real_prefix), file=to)

    def kth_smallest(self, k: int, current: TreeNode) -> TreeNode:
        """
            Finds the kth smallest value by key in the subtree rooted at current.

            Args:
            - k : kth smallest
            - current: current Treenode

            Raises:
            - 
            - 

            Returns:
            - result: treenode that is the kth smallest.

            Complexity:
            - Worst case: O(n), n : the number of nodes.
            - Best case: O(1) when k = root.        
        """
    
        if current.left == None:
            left_subtree_size = 0
        else:
            left_subtree_size = current.left.subtree_size

        if self.is_leaf(current = current):
            if k != 1:
                return None
            return current 
        elif k == left_subtree_size + 1:
            return current
        elif k < left_subtree_size + 1:
            return self.kth_smallest(k = k , current = current.left)
        else:
            return self.kth_smallest(k = (k - (left_subtree_size + 1)) , current = current.right)
    
    def get_sorted_array(self) -> ArrayR[I]:
        """
            Sorts the array in order - ascending

            Args:
            - self

            Raises:
            - 
            - 

            Returns:
            - result: ArrayR - array with sorted elements

            Complexity: (from get_sorted_array_aux)
            - Worst case: O(n), n : the number of nodes.
            - Best case: O(1).      
        """

        sorted_array : ArrayR[I] = ArrayR(length = len(self))
        if self.root.left == None:
            index = 0
        else:
            index = self.root.left.subtree_size
        sorted_array[index] = self.root.item
        self.get_sorted_array_aux(current = self.root.left , array = sorted_array , parent_index = index , is_left = True)
        self.get_sorted_array_aux(current = self.root.right , array = sorted_array , parent_index = index , is_left = False)
        return sorted_array
      
    """
            Auxilary method for get_sorted_array

            Args:
            - self
            - current : TreeNode class
            - array : ArrayR object
            - parent_index : int - gives the index in the array of the parent node
            - is_left : bool - to determine whether to go left or right

            Raises:
            - 
            - 

            Returns:
            - None

            Complexity:
            - Worst case: O(n), n : the number of nodes.
            - Best case: O(1).        
        """
    def get_sorted_array_aux(self, current : TreeNode , array : ArrayR , parent_index : int , is_left : bool) -> None:
        if current == None:
            return
        if current.left == None:
            left_subtree_size = 0
        else:
            left_subtree_size = current.left.subtree_size

        if current.right == None:
            right_subtree_size = 0
        else:
            right_subtree_size = current.right.subtree_size
        
        if is_left == True:
            index = parent_index - right_subtree_size - 1
        else:
            index = parent_index + left_subtree_size + 1

        array[index] = current.item

        self.get_sorted_array_aux(current = current.left , array = array , parent_index = index , is_left = True)
        self.get_sorted_array_aux(current = current.right , array = array , parent_index = index , is_left = False)

        return
