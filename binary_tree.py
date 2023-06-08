class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            
            self.root = new_node
             
        else:
            current=self.root
            
            while True:
                if val<current.val:
                    if current.left is None:
                        current.left=Node(val)
                         
                        break
                    else:
                        current=current.left
                elif val>current.val:
                    if current.right is None:
                        current.right=Node(val)
                        
                        break
                    else:
                        current=current.right
                
       
    def search(self, val):
        current = self.root
        while current is not None:
            if current.val<val:
                current=current.right
            elif current.val >val:
                current=current.left
            elif current.val==val:
                return current.val
    def preorder_recursive(self, node):
        if node:
            print(node.val)
            self.preorder_recursive(node.left)
           
            self.preorder_recursive(node.right)
        else:    
            return
def isSubtree( root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if root is None:
            return subRoot is None
        if subRoot is None:
            return True
        
        if isSameTree(root, subRoot):
            return True
        
        return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
    
        
        
def isSameTree( p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
       
        if p is None and q is None:
            return True
        if p and q and p.val==q.val:
            a=isSameTree(p.left,q.left)
            b=isSameTree(p.right,q.right)
            return a and b
def rightSideView(root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
             return []
        queue = [root]
        
        result = []
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
            result.append(level)
        #  ******** return result if it is level order treversal **********
        res=[] 
        for ele in result:
            res.append(ele[-1])
        return res
tree = BinaryTree()
tree.insert(3)
tree.insert(4)
print(rightSideView(tree.root))

# tree.insert(5)
# tree.insert(2)

# tree.insert(7)
# tree.insert(6)

# tree.preorder_recursive(tree.root)
# tree1 = BinaryTree()
# tree1.insert(5)
# tree1.insert(3)
# tree1.insert(4)
# tree1.insert(2)

# tree1.insert(7)
# tree1.insert(6)
# print(isSameTree(tree.root,tree1.root))
# print(isSubtree(tree.root,tree1.root))


# print(tree.search(1)) # 7
#     5
#   / / \
#  3  6 7
# / \
# 1 2
# 5 3 1