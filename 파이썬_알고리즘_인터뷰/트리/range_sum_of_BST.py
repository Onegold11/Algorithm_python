import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST1(root: TreeNode, L: int, R: int) -> int:
    if not root:
        return 0

    return (root.val if L <= root.val <= R else 0) + rangeSumBST1(root.left, L, R) + rangeSumBST1(root.right, L, R)


def rangeSumBST2(root: TreeNode, L: int, R: int) -> int:
    def dfs(node: TreeNode):
        if not root:
            return 0
        if node.val < L:
            return dfs(node.right)
        elif node.val > R:
            return dfs(node.left)
        return node.val + dfs(node.left) + dfs(node.right)

    return dfs(root)


def rangeSumBST3(root: TreeNode, L: int, R: int) -> int:
    stack, sum = [root], 0

    while stack:
        node = stack.pop()
        if node:
            if node.val > L:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
            if L <= node.val <= R:
                sum += node.val
    return sum


def rangeSumBST4(root: TreeNode, L: int, R: int) -> int:
    stack, sum = collections.deque([root]), 0

    while stack:
        node = stack.popleft()
        if node:
            if node.val > L:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
            if L <= node.val <= R:
                sum += node.val
    return sum


if __name__ == '__main__':
    root = [10, 5, 15, 3, 7, None, 18]
    L, R = 7, 15
