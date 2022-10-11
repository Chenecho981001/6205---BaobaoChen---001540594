from collections import deque, defaultdict


def isSymmetric(root):
    # dfs method
    if not root: return True
    def dfs(left, right):
        if not left and not right: return True
        if not left or not right: return False
        if left.val != right.val: return False
        return dfs(left.left, right.right) and dfs(left.right, right.left)
    return dfs(root.left, root.right)
#  time on
#  space on



def maxDepth(root):
    def dfs(root):
        if not root: return 0
        left = dfs(root.left)
        right = dfs(root.right)
        return max(left, right) + 1
    return dfs(root)



def rightSideView(root):
    if not root: return []
    queue = deque([root])
    res = []
    while queue:
        path = []
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            path.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(path[-1])
    return res



def zigzagLevelOrder(root):
    if not root: return []
    res = []
    def dfs(root, index):
        if not root: return
        if len(res) < index:
            res.append(deque())
        if index % 2 == 1:
            res[index - 1].append(root.val)
        else:
            res[index - 1].appendleft(root.val)
        dfs(root.left, index + 1)
        dfs(root.right, index + 1)
    dfs(root, 1)
    return res



def verticalOrder(root):
    if not root: return []
    dic = defaultdict(list)
    que = [(root, 0)]
    while que:
        cur, offset = que.pop(0)
        dic[offset].append(cur.val)
        if cur.left:
            que.append((cur.left, offset - 1))
        if cur.right:
            que.append((cur.right, offset + 1))
    res = []
    for offset, lists in sorted(dic.items(),key = lambda x: x[0]):
        res.append(lists)
    return res



def widthOfBinaryTree(root):
    queue = deque()
    if not root: return 0
    queue.append((root, 1))
    res = 0
    while queue:
        size = len(queue)
        path = []
        for i in range(size):
            node, val = queue.popleft()
            path.append(val)
            if node.left:
                queue.append((node.left, 2 * val))
            if node.right:
                queue.append((node.right, 2 * val + 1))
        res = max(res, path[-1] - path[0] + 1)
    return res



def lowestCommonAncestor(root, p, q):
    if not root: return root
    if root == p or root == q:
        return root
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    if not left and not right: return
    if not left and right: return right
    if left and not right:
        return left
    else:
        return root



def findLeaves(root):
    def dfs(root):
        if not root: return 0
        l, r = dfs(root.left), dfs(root.right)
        depth = max(l, r) + 1
        res[depth].append(root.val)
        return depth

    res = defaultdict(list)
    dfs(root)
    return [v for v in res.values()]



