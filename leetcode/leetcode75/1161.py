# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        maxSum = -inf
        lv = 0
        maxLv = 0
        while q:
            lv += 1
            lvSum = 0
            for i in range(len(q)):
                node = q.popleft()
                lvSum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if maxSum < lvSum:
                maxSum = lvSum
                maxLv = lv
        return maxLv
