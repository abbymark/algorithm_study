from typing import Optional
import collections

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# iterative dfs
def maxDepth(root: Optional[TreeNode]) -> int:
        
    stack = []
    stack.append((root, 1))
    max_depth = 0
    while stack:
        node, depth = stack.pop()
        if node:
            stack.append((node.right, depth+1))
            stack.append((node.left, depth+1))
            
            if depth > max_depth:
                max_depth = depth
    
    return max_depth

# recursive dfs
def maxDepth(root: Optional[TreeNode]) -> int:
        
    def dfs(node):
        if not node:
            return 0
        else:
            return max(dfs(node.left) + 1, dfs(node.right) + 1)
    
    return dfs(root)

# bfs
def maxDepth(root: Optional[TreeNode]) -> int:
        
    queue = collections.deque()
    queue.append(root)
    
    if not root:
        return 0
    else:
        max_depth = 0
    
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        
        max_depth += 1
    
    return max_depth