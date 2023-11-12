from Set_AVL_Tree import BST_Node, Set_AVL_Tree
#######################################
# DO NOT REMOVE THIS IMPORT STATEMENT #
# DO NOT MODIFY IMPORTED CODE         #
#######################################

def sum(A):
    if A.sum: return A.sum
    return 0

def max_prefix_(A):
    if A.max_prefix: return A.max_prefix
    return 0

class Key_Val_Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self): 
        return "%s,%s" % (self.key, self.val)

class Part_B_Node(BST_Node):
    def subtree_update(A):              # O(1)
        super().subtree_update()
        # DP 定义思想
        A.sum = sum(A.left) + sum(A.right) + A.val
        A.max_prefix, A.max_prefix_key = A.val + A.left.sum, A.item.key
        if A.left and A.val < 0: 
            A.max_prefix, A.max_prefix_key = A.left.sum, A.left.max_prefix_key
        if A.right and A.left.sum + A.val + A.right.max_prefix > A.max_prefix:
            A.max_prefix, A.max_prefix_key = A.left.sum + A.val + A.right.max_prefix, A.right.max_prefix_key

class Part_B_Tree(Set_AVL_Tree):
    def __init__(self): 
        super().__init__(Part_B_Node)

    def max_prefix(self):               # O(1)
        '''
        Output: (k, s) | a key k stored in tree whose
                       | prefix sum s is maximum

        if max_prefix: s = prefix
        
        '''
        k, s = 0, 0
        if self.root: 
            k, s = self.root.max_prefix_key, self.root.max_prefix
        return (k, s)

def tastiest_slice(toppings):
    '''
    Input:  toppings | List of integer tuples (x,y,t) representing 
                     | a topping at (x,y) with tastiness t
    Output: tastiest | Tuple (X,Y,T) representing a tastiest slice 
                     | at (X,Y) with tastiness T
    '''
    B = Part_B_Tree()   # use data structure from part (b)
    X, Y, T = 0, 0, 0
    ##################
    # YOUR CODE HERE #
    ##################
    return (X, Y, T)
