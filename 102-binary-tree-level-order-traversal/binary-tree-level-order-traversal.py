# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


    

        if not root :
            return []
        Q=deque([root])
        res=[]
        while Q:
            level=[]
            for i in range(len(Q)):
                #node nikala chidren dalo
                root=Q.popleft() # root node 

                level.append(root.val)   
                if root.left :
                    Q.append(root.left)
                if root.right:
                    Q.append(root.right)
            res.append(level)
        return res                    