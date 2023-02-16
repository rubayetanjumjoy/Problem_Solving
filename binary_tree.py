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
        
        

tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(1)
tree.insert(2)

tree.insert(7)
tree.insert(6)

tree.preorder_recursive(tree.root)



# print(tree.search(1)) # 7
#     5
#   / / \
#  3  6 7
# / \
# 1 2
# 5 3 1