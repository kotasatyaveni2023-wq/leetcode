# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        from collections import deque
        if root is None:
            return []
        queue = deque([root])
        result = []
        level = 0
        while queue:
            current = []
            for i in range(len(queue)):
                node = queue.popleft()

                current.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if level % 2 == 1:
                current.reverse()

            result.append(current)

            level += 1

        return result
        