# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sumCount = Counter({0:1})

        def dfs(node, currentSum):
            if node is None:
                return 0
            currentSum += node.val
            count = sumCount[currentSum - targetSum]
            sumCount[currentSum] += 1
            count += dfs(node.left, currentSum)
            count += dfs(node.right, currentSum)

            sumCount[currentSum] -= 1
            return count
        return dfs(root, 0)
