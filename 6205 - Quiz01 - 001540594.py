from collections import deque;

#problem 01
from collections import deque

def rotate(nums,k):
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
            pos =(j + k) % len(nums)
            nums[pos],curr = curr,nums[pos]
            j = pos
            count += 1
        i += 1



#problem 02
def isSameTree(p, q):
    if not p and not q:
        return 1
    if not p or not q:
        return 0
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


#problem 03
def levelOrder(root):
        # Corner case.
    if not root:
        return []

    nodes = []  # Result nodes.
    queue = deque([root])
    # BFS on tree queue.
    while queue:
        levelLen = len(queue)
        levelNodes = []
        for i in range(levelLen):
            curNode = queue.popleft()
            levelNodes.append(curNode.val)
            if curNode.left:
                queue.append(curNode.left)
            if curNode.right:
                queue.append(curNode.right)
        nodes.append(levelNodes)
    return nodes
