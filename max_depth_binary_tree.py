 
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, depth):
            if not root: return depth
            a=dfs(root.left, depth + 1) 
            b=dfs(root.right, depth + 1)  
            return max(a,b)          
        return dfs(root, 0)
    

#  2
# /\
# 1 3
# 
root=TreeNode(5)
root.left=TreeNode(1)
root.right=TreeNode(6)
root.right.right=TreeNode(10)
count=Solution()
print(count.maxDepth(root))
        
            
