# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        queue = deque([root])
        while queue:
            lv = len(queue)
            for i in range(lv):
                cNode = queue.popleft()
                if i == lv - 1:
                    ans.append(cNode.val)
                if cNode.left:
                    queue.append(cNode.left)
                if cNode.right:
                    queue.append(cNode.right)
        return ans
