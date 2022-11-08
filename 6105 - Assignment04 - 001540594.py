# Question1
class ListNode:
    def __init__(val, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedListToBST(head):
    if not head:
        return None
    mid = findMin(head)
    node = TreeNode(mid.val)
    if mid == head:
        return node
    node.left = sortedListToBST(head)
    node.right = sortedListToBST(mid.next)
    return node


def findMin(head):
    prev = None
    slow = head
    fast = head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    if prev:
        prev.next = None
    return slow



# Question2
class Node(object):
    def __init__(val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def treeToDoublyList(self, root):
    def helper(node):
        head = tail = node
        if node.left:
            head, tailL = helper(node.left)
            tailL.right = node
            node.left = tailL
        if node.right:
            headR, tail = helper(node.right)
            node.right = headR
            headR.left = node
        return head, tail

    if not root:
        return None
    head, tail = helper(root)
    head.left = tail
    tail.right = head
    return head



# Question3
def isValidBST(root):
    def dfs(max_value, min_value, node):
        if not node:
            return True
        if node.val >= max_value or node.val <= min_value:
            return False

        return dfs(node.val, min_value, node.left) and dfs(max_value, node.val, node.right)

    return dfs(float("inf"), -float("inf"), root)



# question4
def recoverTree(root):
    stack = []
    x = y = pred = None
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if pred and root.val < pred.val:
            y = root
            if x is None:
                x = pred
            else:
                break
        pred = root
        root = root.right
    x.val, y.val = y.val, x.val



# question5
class BSTIterator(object):
    def __init__(root):
        self.nodes_sorted = []
        self.index = -1
        self._inorder(root)

    def _inorder(root):
        if not root:
            return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)

    def next():
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext():
        return self.index + 1 < len(self.nodes_sorted)



# question6
class Codec:
    def serialize(root):
        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []

        return " ".join(map(str, postorder(root)))

    def deserialize(data):
        def helper(lower, upper):
            if not data or data[-1] < lower or data[-1] > upper:
                return None
            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root

        data = [int(x) for x in data.split(" ") if x]
        return helper(float("-inf"), float("inf"))



# question7
class Solution:
    previous = None
    inorder_successor_node = None

    def inorderSuccessor(root, p):

        self.previous, self.inorder_successor_node = None, None

        # Case 1: We simply need to find the leftmost node in the subtree rooted at p.right.
        if p.right:
            leftmost = p.right
            while leftmost.left:
                leftmost = leftmost.left

            self.inorder_successor_node = leftmost

        # Case 2: We need to perform the standard inorder traversal and keep track of the previous node.
        else:
            self.inorderCase2(root, p)

        return self.inorder_successor_node

    def inorderCase2(node: 'TreeNode', p: 'TreeNode'):

        if not node:
            return

        # Recurse on the left side
        self.inorderCase2(node.left, p)

        # Check if previous is the inorder predecessor of node
        if self.previous == p and not self.inorder_successor_node:
            self.inorder_successor_node = node
            return

        # Keeping previous up-to-date for further recursions
        self.previous = node

        # Recurse on the right side
        self.inorderCase2(node.right, p)



# question8
def rangeSumBST( root, low, high):
    def dfs(node):
        nonlocal ans
        if node:
            if low <= node.val <= high:
                ans += node.val
            if low < node.val:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)
    ans = 0
    dfs(root)
    return ans