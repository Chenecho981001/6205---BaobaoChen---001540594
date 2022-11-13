from collections import defaultdict

class Tree:
    pass
class ListNode:
    pass


def question1(root):
    if not root:
        return
    queue = [root];
    while queue:
        l = len(queue);
        for i in range(l):
            if i == 0:
                queue[i].next = None
            else:
                queue[i].next = queue[i-1]
            if queue[i].left:
                queue.append(queue[i].left)
            if queue[i].right:
                queue.append(queue[i].right)
        queue = queue[l:]
    return root
#time:on


def question2(root, parent_node):
    if not root:
        return None
    root.parent = parent_node
    if root.left:
        question2(root.left,root)
    if root.right:
        question2(root.right,root)
    return root
#time:on


def question3(array,root):
    ans = []
    def findRange(root,array):
        if not root:
            return
        if root.val < array[-1] and root.val > array[0]:
            ans.append(root.val)
        if root.left:
            findRange(root.left,array)
        if root.right:
            findRange(root.right,array)
    findRange(array,root)
    return ans
#time:on


def question4(head,node):
    dummy = ListNode()
    dummy.next = head
    ans = []
    prev = dummy
    while head:
        if head.val < node.val:
            prev = prev.next
            head = head.next
    prev.next = node
    node.next = head
    return dummy.next
#time:on


def question5(array1,array2):
    dic = defaultdict(int)
    for index,val in enumerate(array1):
        if val not in dic:
            dic[val] = index
    ans = []
    for i in array2:
        if i not in dic:
            ans.append(-1)
        else:
            ans.append(dic[i])
    return ans
#time:on




