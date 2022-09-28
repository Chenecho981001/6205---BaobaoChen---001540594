#Problem 01
def rotateRight(head, k):
    # calculate the length of the list , then we k % length = k
    # remove the k nodes of the end of the list, and move it to the front of the list
    if not head or not head.next: return head
    one = head
    length = 0
    tail = head
    cur = None
    while tail:
        length += 1
        cur = tail
        tail = tail.next
    k = k % length
    if k == 0:
        return head
    pointer = length - k - 1
    dummy1 = ListNode()
    dummy1.next = head
    while pointer:
        pointer -= 1
        head = head.next
    dummy2 = ListNode(0)
    dummy2.next = head.next
    cur.next = dummy1.next
    head.next = None
    return dummy2.next
# time on
# space o1


#Problem 02
def removeElements(head, val):
    res = []
    while head:
        if head.val != val:
            res.append(head)
        head = head.next
    cur = dummy = ListNode()
    for i in range(len(res)):
        cur.next = res[i]
        cur = cur.next
    cur.next = None
    return dummy.next


#Problem 03
def swapNodes(head, k):
    left = right = head
    for i in range(k - 1):
        right = right.next
    forward = right
    while right.next:
        left = left.next
        right = right.next
    reverse = left
    forward.val, reverse.val = reverse.val, forward.val
    return head


#Problem 04
def splitListToParts(self, root, k):
    ans = [None for i in range(k)]
    ans[0] = root
    for i in range(1, k):
        if ans[i - 1]:
            ans[i] = ans[i - 1].next
    while ans[k - 1]:
        for i in range(k - 1):
            ans[k - 1] = ans[k - 1].next
            if not ans[k - 1]:
                break
            for j in range(i, k - 1):
                ans[j] = ans[j].next
        if ans[k - 1]:
            ans[k - 1] = ans[k - 1].next
    for i in range(k - 1, 0, -1):
        if ans[i - 1]:
            ans[i] = ans[i - 1].next
            ans[i - 1].next = None
    ans[0] = root
    return ans



#Problem 05
def insert(head,insertVal):
    if head == None:
        newNode = Node(insertVal, None)
        newNode.next = newNode
        return newNode
    prev, curr = head, head.next
    toInsert = False
    while True:
        if prev.val <= insertVal <= curr.val:
            toInsert = True
        elif prev.val > curr.val:
            if insertVal >= prev.val or insertVal <= curr.val:
                toInsert = True
        if toInsert:
            prev.next = Node(insertVal, curr)
            return head
        prev, curr = curr, curr.next
        if prev == head:
            break
    prev.next = Node(insertVal, curr)
    return head



