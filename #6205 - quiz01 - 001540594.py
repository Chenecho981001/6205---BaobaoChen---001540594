#6205 - quiz01 - 001540594

#problem 01
from collections import deque


def rotate(nums, k):
    k = k % len(nums)
    n = len(nums)
    i = 0
    count = 0
    while count < n:
        pos = (i + k) % len(nums)
        curr = nums[pos]
        nums[pos] = nums[i]
        count += 1
        j = pos
        while j != i and count < n:
            pos = (j + k) % len(nums)
            nums[pos], curr = curr, nums[pos]
            j = pos
            count += 1
        i += 1


#problem 02
def isSameTree(p, q):
    def t(n):
        return n and (n.val, t(n.left), t(n.right))
    return t(p) == t(q)


#problem 03
def levelOrder(root):
        # Corner case.
    if not root:
        return []

    nodes = []  # Result nodes.
    nodeDeque = deque([root])
    # BFS on tree using nodeDeque.
    while nodeDeque:
        levelLen = len(nodeDeque)
        levelNodes = []
        for i in range(levelLen):
            curNode = nodeDeque.popleft()
            levelNodes.append(curNode.val)
            if curNode.left:
                nodeDeque.append(curNode.left)
            if curNode.right:
                nodeDeque.append(curNode.right)
        nodes.append(levelNodes)
    return nodes
