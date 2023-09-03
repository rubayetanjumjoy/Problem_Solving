class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#       5
#     /  \
#   3    6
# /
# 2      /\
#      9 10

#queue=[,,six.ten] 
# result=[[5],[3,6][2,9,10]]
def level_order(root):
    result=[]
    if root is None:
        return []
    queue=[root]
    while queue:
        level=[]
        for i in range(len(queue)):
            node=queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        result.append(level)
    return result





def tree_print(root):
    if root is None:
        return
    print(root.val)
    tree_print(root.left)
    tree_print(root.right)

root=TreeNode(5)
root.left=TreeNode(3)
root.right=TreeNode(6)

# root.left.right=TreeNode(2)
# root.right=TreeNode(6)
# root.right.right=TreeNode(10)
# root.right.left=TreeNode(9)

# tree_print(root)
print(level_order(root))
#       5
#     /  \
#   3    6
# /
# 
#  

def isValidBST(root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 3->, -inf ,5
        def dfs(node, min_val, max_val):
            if not node:
                return True
          
            if not min_val < node.val < max_val:
                return False
            left=dfs(node.left, min_val, node.val)
            right=dfs(node.right, node.val, max_val)
            return  left==right 
        return dfs(root, float('-inf'), float('inf'))
print(isValidBST(root))


