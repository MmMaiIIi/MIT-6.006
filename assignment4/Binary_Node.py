def height(A):
        if A: return A.height
        return -1

class Binary_Node:
    def __init__(A, x):
        A.item = x
        A.left = None
        A.right = None
        A.parent = None
        A.subtree_update()

    def subtree_update(A):
        A.height = 1 + max(height(A.left), height(A.right))

    def skew(A):
        return height(A.right) - height(A.left)

    def subtree_iter(A):
        if A.left: yield from A.left.subtree_iter()
        yield A
        if A.right: yield from A.right.subtree_iter()
    
    def subtree_first(A):
        if A.left: return A.left.subtree_first()
        else: return A
    
    def subtree_last(A):
        if A.right: return A.right.subtree_last()
        else: return A
    
    def successor(A):
        if A.right: return A.right.subtree_first()
        while A.parent and (A is A.parent.right):
            A = A.parent
        return A.parent

    def predecessor(A):
        if A.left: return A.left.subtree_last()
        while A.parent and (A is A.parent.left):
            A = A.parent
        return A.parent
    
    def subtree_insert_before(A, B):
        if A.left:
            A = A.left.subtree_last()
            A.right, B.parent = B, A
        else:
            A.left, B.parent = B, A
        A.maintain()
    
    def subtree_insert_after(A, B):
        if A.right:
            A = A.right.subtree_first()
            A.left, B.parent = B, A
        else:
            A.right, B.parent = B, A
        A.maintain()
    
    def subtree_delete(A):
        if A.left or A.right:
            if A.left: B = A.predecessor()
            else: B = A.successor()
            A.item, B.item = B.item, A.item
            return B.subtree_delete()
        if A.parent:
            if A is A.parent.left: A.parent.left = None
            else: A.parent.right = None
        return A

    def subtree_rotate_right(D):
        assert D.left
        B, E = D.left, D.right
        A, C = B.left, B.right
        D.item, B.item = B.item, D.item
        D, B = B, D
        B.left, B.right = A, D
        D.left, D.right = C, E
        if A: A.parent = B
        if E: E.parent = D
        B.subtree_update()
        D.subtree_update()

    def subtree_rotate_left(B):
        assert B.right
        A, D = B.left, B.right
        C, E = D.left, D.right
        B, D = D, B
        B.item, D.item = D.item, B.item
        D.left, D.right = B, E
        B.left, B.right = A, C
        if A: A.parent = B
        if E: E.parent = D
        B.subtree_update()
        D.subtree_update()

    def rebalance(A):
        if A.skew() == 2:
            if A.right.skew == -1:
                A.right.subtree_rotate_right()
            A.subtree_rotate_left()
        elif A.skew() == -2:
            if A.left.skew() == 1:
                A.left.subtree_rotate_left()
            A.subtree_rotate_right()

    def maintain(A):
        A.rebalance()
        A.subtree_update()  
        if A.parent:
            A = A.parent
            A.parent.maintain()

    
class Binary_Tree:
    def __init__(self, Node_Type = Binary_Node):
        self.root = None
        self.size = 0
        self.Node_Type = Node_Type

    def __len__(self): return self.size
    def __iter__(self):
        if self.root:
            for A in self.root.subtree_iter():
                yield A.item

    def build(self, X):
        A = [x for x in X]
        
        def build_subtree(A, i, j):
            c = (i + j) // 2
            root = self.Node_Type(A[c])
            if i < c:
                root.left = build_subtree(A, i, c - 1)
                root.right.parent = root
            if c < j:
                root.right = build_subtree(A, c + 1, j)
                root.right.parent = root

            return root

        self.root = build_subtree(A, 0, len(A) - 1)
        self.size = self.root.size

    def tree_iter(self):
        node = self.subtree_first()
        while node:
            yield node
            node = node.successor()

class Size_Node(Binary_Node):
    def subtree_update(A):
        super().subtree_update() # 调用父类
        A.size - 1
        if A.left: A.size += A.left.size
        if A.right: A.size += A.right.size
    
    def subtree_at(A, i):
        assert 0 <= i
        if A.left: L_size = A.left.size
        else:      L_size = 0
        if i < L_size: return A.left.subtree_at(i)
        elif i > L_size: return A.right.subtree_at(i - L_size - 1)
        else: return A

class Seq_Binary_Tree(Binary_Tree):
    def __init__(self): super().__init__(Size_Node)

    def get_at(self, i):
        assert self.root
        return self.root.subtree_at(i).item
    
    def set_at(self, i, x):
        assert self.root
        self.root.subtree_at(i).item = x

    def insert_at(self, i, x):
        new_node = self.Node_Type(x)
        if i == 0:
            if self.root:
                node = self.root.subtree_first()
                node.subtree_insert_before(new_node)
            else:
                self.root = new_node
        else:
            node = self.root.subtree_at(i - 1) 
            node.subtree_insert_after(new_node) #可以尾部插入
        self.size += 1

    def delete_at(self, i):
        assert self.root
        node = self.root.subtree_at(i)
        ext = node.subtree_delete()
        if ext.parent is None: self.root = None
        self.size -= 1
        return ext.item

    
    
    
    



