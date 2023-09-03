"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
       
        # output.append(root.val)
        # for ele in root.children:
        #     self.preorder(ele)
        # print(output)
        output=[]
        self.bfs(root,output)
        return output
        

    def bfs(self,root,output):
        if root is None: return
       
        output.append(root.val)
         
        
        for ele in root.children:
             
             self.bfs(ele,output)
        # output.append(root.val) // if we need to print depth first search (dfs)
         
        
             
        