import unittest
from ed_utils.decorators import number, visibility
from ed_utils.timeout import timeout

from bst import BinarySearchTree
from referential_array import ArrayR

class BSTTest(unittest.TestCase):

    @timeout()
    @number("1.1")
    def test_p1(self):
        BST = BinarySearchTree()
        BST[95] = 1
        BST[73] = 2
        BST[99] = 3
        BST[50] = 4
        BST[85] = 5
        BST[80] = 6
        BST[75] = 7
        BST[74] = 8
        BST[72] = 9
        BST[93] = 10
        BST[91] = 11
        BST[97] = 12
        BST[5]  = 13
        BST[100] = 14


        minimal = BST.get_minimal(BST.root)
        self.assertEqual(minimal.key, 5)
        self.assertEqual(minimal.item, 13)

        minimal = BST.get_minimal(BST.root.right)
        self.assertEqual(minimal.key, 97)
        self.assertEqual(minimal.item, 12)

        minimal = BST.get_minimal(BST.root.left.left.left)
        self.assertEqual(minimal.key, 5)
        self.assertEqual(minimal.item, 13)

        minimal = BST.get_minimal(BST.root.left.right)
        self.assertEqual(minimal.key, 74)
        self.assertEqual(minimal.item, 8)



        successor = BST.get_successor(BST.root)
        self.assertEqual(successor.key, 97)
        self.assertEqual(successor.item, 12)

        successor = BST.get_successor(BST.root.left)
        self.assertEqual(successor.key, 74)
        self.assertEqual(successor.item, 8)

        successor = BST.get_successor(BST.root.left.right)
        # self.assertEqual(successor, None)
        self.assertEqual(successor.key, 91)
        self.assertEqual(successor.item, 11)


        successor = BST.get_successor(BST.root.left.left)
        self.assertEqual(successor.key, 72)
        self.assertEqual(successor.item, 9)

        successor = BST.get_successor(BST.root.left.left.left)
        self.assertEqual(successor, None)

        successor = BST.get_successor(BST.root.right)
        self.assertEqual(successor.key, 100)
        self.assertEqual(successor.item, 14)

        successor = BST.get_successor(BST.root.left.right.left)
        self.assertEqual(successor, None)

        BST.draw()
        
        array = BST.get_sorted_array()
        for i in range (len(array)):
            print("array is " , array[i])





    @timeout()
    @number("1.2")
    def test_p2(self):
        BST = BinarySearchTree()
        BST[95] = 1
        BST[73] = 2
        BST[99] = 3
        self.assertEqual(BST.root.subtree_size, 3)
        BST[50] = 4
        BST[85] = 5
        BST[80] = 6

        self.assertEqual(BST.root.subtree_size, 6)
        self.assertEqual(BST.root.left.subtree_size, 4)
        self.assertEqual(BST.root.right.subtree_size, 1)
        self.assertEqual(BST.root.left.left.subtree_size, 1)
        self.assertEqual(BST.root.left.right.subtree_size, 2)
        self.assertEqual(BST.root.left.right.left.subtree_size, 1)

        try:
            BST[80] = 6
            BST[50] = 4
            BST[85] = 5
            BST[80] = 6
        except ValueError:
            print("went to ValueError")
            self.assertEqual(BST.root.subtree_size, 6)
            self.assertEqual(BST.root.left.subtree_size, 4)
            self.assertEqual(BST.root.right.subtree_size, 1)
            self.assertEqual(BST.root.left.left.subtree_size, 1)
            self.assertEqual(BST.root.left.right.subtree_size, 2)
            self.assertEqual(BST.root.left.right.left.subtree_size, 1)
        else:
            print("went to else")


        del BST[73]
        self.assertEqual(BST.root.subtree_size, 5)
        self.assertEqual(BST.root.left.subtree_size, 3)
        self.assertEqual(BST.root.right.subtree_size, 1)
        self.assertEqual(BST.root.left.left.subtree_size, 1)
        self.assertEqual(BST.root.left.right.subtree_size, 1)
        # self.assertEqual(BST.root.left.right.left.subtree_size, 1)

        del BST[95]
        self.assertEqual(BST.root.subtree_size, 4)
        self.assertEqual(BST.root.left.subtree_size, 3)
        # self.assertEqual(BST.root.right.subtree_size, 1)
        self.assertEqual(BST.root.left.left.subtree_size, 1)
        self.assertEqual(BST.root.left.right.subtree_size, 1)
        # self.assertEqual(BST.root.left.right.left.subtree_size, 1)



    @timeout()
    @number("1.3")
    def test_p3(self):
        BST = BinarySearchTree()
        BST[95] = 1
        BST[73] = 2
        BST[99] = 3
        BST[50] = 4
        BST[85] = 5
        BST[80] = 6
        BST[83] = 7
        BST[86] = 8
        BST[51] = 9

        BST.draw()

        kth = BST.kth_smallest(1, BST.root)
        self.assertEqual(kth.key, 50)
        self.assertEqual(kth.item, 4)

        kth = BST.kth_smallest(2, BST.root)
        self.assertEqual(kth.key, 51)
        self.assertEqual(kth.item, 9)

        kth = BST.kth_smallest(3, BST.root)
        self.assertEqual(kth.key, 73)
        self.assertEqual(kth.item, 2)

        kth = BST.kth_smallest(4, BST.root)
        self.assertEqual(kth.key, 80)
        self.assertEqual(kth.item, 6)

        kth = BST.kth_smallest(5, BST.root)
        self.assertEqual(kth.key, 83)
        self.assertEqual(kth.item, 7)

        kth = BST.kth_smallest(6, BST.root)
        self.assertEqual(kth.key, 85)
        self.assertEqual(kth.item, 5)

        kth = BST.kth_smallest(7, BST.root)
        self.assertEqual(kth.key, 86)
        self.assertEqual(kth.item, 8)

        kth = BST.kth_smallest(8, BST.root)
        self.assertEqual(kth.key, 95)
        self.assertEqual(kth.item, 1)

        kth = BST.kth_smallest(9, BST.root)
        self.assertEqual(kth.key, 99)
        self.assertEqual(kth.item, 3)

    @timeout()
    @number("1.4")
    def test_p4(self):
        BST = BinarySearchTree()
        BST[95] = 3
        BST[73] = 2
        BST[50] = 1
        

        kth = BST.kth_smallest(1, BST.root)
        self.assertEqual(kth.key, 50)
        self.assertEqual(kth.item, 1)

        BST[1] = 1
        BST[5] = 4
        BST[3] = 2
        BST[4] = 3
        

        kth = BST.kth_smallest(4, BST.root)
        self.assertEqual(kth.key, 5)
        self.assertEqual(kth.item, 4)

        # kth = BST.kth_smallest(2, BST.root.left.right)
        # self.assertEqual(kth.key, 85)
        # self.assertEqual(kth.item, 5)

        # kth = BST.kth_smallest(5, BST.root)
        # self.assertEqual(kth.key, 95)
        # self.assertEqual(kth.item, 1)


