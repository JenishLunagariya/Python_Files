"""Linked List Problems"""
class Node:
    '''for each node'''
    def __init__(self,data=None) -> None:
        self.data = data
        self.next = None
    def __repr__(self) -> str:
        return str(self.data)
    def __del__(self):
        value = self.data
        if value!= None:
            del self.next
            del self.data
class LinkedListS:
    '''represents start of the linked list'''
    def __init__(self,nodes = None) -> None:
        self.head = None
        self.tail = None
        if nodes is not None and len(nodes) != 0:
            node = Node(data = nodes.pop(0))
            self.head  = node
            for ele in nodes:
                node.next = Node(ele)
                node = node.next
            self.tail = node
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return "->".join(nodes)
    def __iter__(self):
        node = self.head
        while node is  not None:
            yield node
            node = node.next
    def __len__(self):
        length = 0
        node =self.head
        while node is not None:
            length+=1
            node = node.next
        return length
    def insertAtTail(self,data):
        if self.tail == None:
            node = Node(data)
            self.head = node
            self.tail = node
            return
        node = Node(data=data)
        self.tail.next = node
        self.tail = self.tail.next
    def insertAtPos(self,position,data):
        if position == 1:
            self.insertAtHead(data)
            return
        # travere to position
        temp = self.head
        cnt = 1
        while cnt < position-1:
            temp = temp.next
            cnt+=1
        if temp.next == None:
            self.insertAtTail(data)
            return
        # new node
        node_new = Node(data)
        node_new.next = temp.next
        temp.next = node_new
    def deleteNodewithPos(self,position):
        if position==1:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            del temp
            return
        else:
            prev = None
            current = self.head
            cnt = 1
            while cnt<position:
                prev = current
                current = current.next
                cnt+=1
            if current.next == None:
                self.tail = prev
            prev.next = current.next
            current.next = None
            del current 
            return
    def sortLL(self):
        '''sort linked list'''
        # BUG: nested loop not working
        i = self.head
        while i != None:
            initial_i = i
            print("data: ",i.data,"type: ",type(i.data))
            j = self.head.next
            while j!= None:
                initial_j = j
                if i.data > j.data:
                    forward = j.next
                    i.next = forward
                    j.next = i
                j = initial_j.next
            i = initial_i.next
        return self
    def ReverseInKgroup(self,head,k):
        '''reverse LL in group of k nodes.
        ex: k=2, reverse first 2 nodes, then reverse other 2 nodes(3 & 4), go on till tail node.
        k=3, reverse first 3 nodes, then other 3 nodes(4,5 & 6), go on till tail node'''
        if head == None:
            return None
        # revere first k nodes
        prev = None
        curr = head
        forward = None
        cnt=0
        while curr != None and cnt < k:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
            cnt+=1
        # recursion handles further
        if forward!= None:
            head.next = self.ReverseInKgroup(forward,k)
        # return ll
        return prev

    def isCircular(self,head,head_next):
        '''check LL is circular or not, return true/false'''
        if head == None:
            return True
        else:
            temp = head_next
            while temp!=None and temp!= head:
                temp = temp.next
            if temp == head:
                return True
            elif temp == None:
                return False
    

ll = LinkedListS([1,2,3,4,5,6])
print(ll)
'''
# ReverseInKgroup

ll.head = ll.ReverseInKgroup(ll.head,2)
node = ll.head
while node.next!=None:
    node = node.next
ll.tail = node
print(ll)
print("head: ",ll.head)
print("tail: ",ll.tail)
'''

'''
# isCircular
print(ll.isCircular(ll.head,ll.head.next))
'''