# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, currentMax):
            if node is None:
                return 
            if node.val >= currentMax:
                nonlocal goodNode
                goodNode += 1
                currentMax = node.val
            dfs(node.left, currentMax)
            dfs(node.right, currentMax)
        goodNode = 0
        dfs(root, float('-inf'))

        return goodNode
# Reference

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def good_nodes_helper(root, upper_bound):
            if root is None:
                return 0

            if root.val < upper_bound:
                return good_nodes_helper(root.left, upper_bound) + good_nodes_helper(root.right, upper_bound)
            else:
                # case: root.val >= upper_bound
                return 1 + good_nodes_helper(root.left, root.val) + good_nodes_helper(root.right, root.val)

        # if root is None:
        #     return 0

        # left_good_nodes = good_nodes_helper(root.left, root.val)
        # right_good_nodes = good_nodes_helper(root.right, root.val)

        # return left_good_nodes + right_good_nodes + 1

        return good_nodes_helper(root, root.val)
