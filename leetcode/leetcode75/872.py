# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(node, leafV):
            if not node:
                return
            if node.left is None and node.right is None:
                leafV.append(node.val)
                return
            if node.left:
                leaves(node.left, leafV)
            if node.right:
                leaves(node.right, leafV)
        
        leafTree1 = []
        leafTree2 = []

        leaves(root1, leafTree1)
        leaves(root2, leafTree2)
        return leafTree1 == leafTree2
# Reference
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        it1 = LeafIterator(root1)
        it2 = LeafIterator(root2)
        # 逐一对比叶子节点
        while it1.hasNext() and it2.hasNext():
            if it1.next().val != it2.next().val:
                return False
        # 最后应该都完成遍历
        return not it1.hasNext() and not it2.hasNext()

# 一个生成二叉树叶子节点的迭代器
class LeafIterator:
    # 模拟递归过程
    def __init__(self, root: TreeNode):
        self.stk = [root]

    def hasNext(self) -> bool:
        return len(self.stk) > 0

    def next(self) -> TreeNode:
        while len(self.stk) > 0:
            cur = self.stk.pop()
            if cur.left is None and cur.right is None:
                # 发现一个叶子结点
                return cur
            # 先入栈 root.right
            if cur.right is not None:
                self.stk.append(cur.right)
            if cur.left is not None:
                self.stk.append(cur.left)
        return None
