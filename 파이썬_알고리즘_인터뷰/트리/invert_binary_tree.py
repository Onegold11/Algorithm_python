import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree1(root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = invertTree1(root.right), invertTree1(root.left)
        return root


def invertTree2(root: TreeNode) -> TreeNode:
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()

        if node:
            node.left, node.right = node.right, node.left

            queue.append(node.left)
            queue.append(node.right)

    return root


def invertTree3(root: TreeNode) -> TreeNode:
    stack = collections.deque([root])

    while stack:
        node = stack.pop()

        if node:
            node.left, node.right = node.right, node.left

            stack.append(node.left)
            stack.append(node.right)

    return root


def invertTree4(root: TreeNode) -> TreeNode:
    stack = collections.deque([root])

    while stack:
        node = stack.pop()

        if node:
            stack.append(node.left)
            stack.append(node.right)

            node.left, node.right = node.right, node.left

    return root
