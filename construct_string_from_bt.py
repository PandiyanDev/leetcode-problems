"""     
Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

 Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def dfs(root):
            if not root:
                return ""
            if root.right:
                return str(root.val) + "(" + dfs(root.left) + ")" + "(" + dfs(root.right) + ")"
            if root.left:
                return str(root.val) + '(' +dfs(root.left) + ")"
            return str(root.val)

        return dfs(root)

# Construct the tree
## input  is [1, 2, 3, 4] and give input based tree data structure
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = None
root.left.right = TreeNode(4)

# Create an instance of the Solution class
solution_instance = Solution()

# Call the tree2str method
result = solution_instance.tree2str(root)

# Print the result
print(result)
