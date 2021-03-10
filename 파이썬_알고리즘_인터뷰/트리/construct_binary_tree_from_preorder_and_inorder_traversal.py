from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    if inorder:
        index = inorder.index(preorder.pop(0))

        node = TreeNode(inorder[index])
        node.left = buildTree(preorder, inorder[0:index])
        node.right = buildTree(preorder, inorder[index + 1:])

        return node